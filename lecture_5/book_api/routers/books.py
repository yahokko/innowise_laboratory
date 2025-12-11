from fastapi import APIRouter, HTTPException
from sqlalchemy import or_, select, update, delete
from book_api.models import BookModel
from book_api.schemas import BookSchema, BookCreateSchema, BookUpdateSchema
from book_api.database import SessionDep

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", summary="Add a new book")
async def add_book(book: BookCreateSchema, session: SessionDep) -> dict:
    """
    Add a new book to the database.
    """
    new_book = BookModel(
        title = book.title,
        author = book.author,
        year = book.year
    )

    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)

    return {"added": True, "book": BookSchema.model_validate(new_book)}


@router.get("/", summary="Get all books", response_model=list[BookSchema])
async def get_all_books(session: SessionDep) -> list:
    """
    Return a list of all books.
    """
    query = select(BookModel)
    result = await session.execute(query)

    return result.scalars().all()


@router.delete("/{book_id}", summary="Delete a book")
async def delete_book(book_id: int, session: SessionDep) -> dict:
    """
    Delete a book by its ID.
    Raises 404 if not found.
    """
    stmt = (
        delete(BookModel).filter_by(id=book_id)
    )
    result = await session.execute(stmt)

    # result.rowcount sometimes returns -1 with SQLite, so check both
    if result.rowcount in (0, -1):
        raise HTTPException(status_code=404, detail="Book not found")

    await session.commit()
    return {"deleted": True, "book_id": book_id}


@router.put("/{book_id}", summary="Update an existing book")
async def update_book(
    book_id: int,
    update_data: BookUpdateSchema,
    session: SessionDep
    ) -> dict:
    """
    Update a book by its ID.
    Only provided fields are updated.
    """
    cleaned_data = update_data.model_dump(exclude_none=True)

    if not cleaned_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    stmt = (
        update(BookModel)
        .where(BookModel.id == book_id)
        .values(**cleaned_data)
        )
    
    result = await session.execute(stmt)

    if result.rowcount in (0, -1):
        raise HTTPException(status_code=404, detail="Book not found")
    
    await session.commit()

    return {"updated": True, "book_id": book_id, "changes": cleaned_data}



@router.get("/search/", summary="Search books by any field", response_model=list[BookSchema])
async def get_book_by(
    session: SessionDep,
    book_title: str | None = None,
    book_author: str | None = None,
    book_year: int | None = None
    ) -> list:
    """
    Search for books by title, author, or year.
    Multiple conditions are combined with OR.
    """
    conditions = []

    if book_title:
        conditions.append(BookModel.title.ilike(f"%{book_title}%"))

    if book_author:
        conditions.append(BookModel.author.ilike(f"%{book_author}%"))

    if book_year:
        conditions.append(BookModel.year == book_year)
        
        
    if not conditions:
        raise HTTPException(status_code=400, detail="No data to search")
    
    query = select(BookModel).where(or_(*conditions))
    result = await session.execute(query)

    return result.scalars().all()