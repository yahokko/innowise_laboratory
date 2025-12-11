from sqlalchemy.orm import Mapped, mapped_column
from book_api.database import Base


class BookModel(Base):
    """
    SQLAlchemy ORM model for books table.
    """
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int|None] = mapped_column(nullable=True)
