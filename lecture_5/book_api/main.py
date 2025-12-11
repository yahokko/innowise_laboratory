from fastapi import FastAPI
from book_api.database import engine, Base
from book_api.routers import books

app = FastAPI(
    title="Books API",
    description="Simple CRUD API for managing books"
)

@app.on_event("startup")
async def setup_database():
    """
    Create the database schema on application startup.

    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return {"Database created.": True}

# Include all book-related routes
app.include_router(books.router)