from pydantic import BaseModel, Field, create_model
from typing import Optional


class BookSchema(BaseModel):
    """
    Schema used for returning Book objects (response model).
    """
    model_config = {
        "from_attributes": True,  # Allow reading ORM objects
        "extra": "forbid"         # Reject undefined fields
        }
    id : int = Field(examples=[1])
    title: str = Field(examples=["The Little Prince"])
    author: str = Field(examples=["Antoine de Saint-Exupéry"])
    year: int | None = Field(default=None, examples=[1943])


class BookCreateSchema(BaseModel):
    """
    Schema used when creating a new Book (client input).
    """

    title: str = Field(examples=["The Little Prince"])
    author: str = Field(examples=["Antoine de Saint-Exupéry"])
    year: int | None = Field(default=None, examples=[1943])


# Dynamic schema for partial updates (PATCH/PUT)
BookUpdateSchema = create_model(
    'BookUpdateSchema',
    **{
        name: (Optional[field.annotation], None)
        for name, field in BookSchema.model_fields.items()
        if name != "id"
        }
)