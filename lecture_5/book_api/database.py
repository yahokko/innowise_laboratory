from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated, AsyncGenerator
from fastapi import Depends


class Base(DeclarativeBase):
    """Base class for ORM models."""

    pass


# Async SQLite engine
engine = create_async_engine(
    url='sqlite+aiosqlite:///books.db',
    echo= True
    )


# Session factory
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides an async SQLAlchemy session.
    """
    async with async_session() as session:
        yield session


# Type alias for FastAPI dependency injection
SessionDep = Annotated[AsyncSession, Depends(get_session)]