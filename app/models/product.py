from sqlmodel import Field, SQLModel

from app.core.models import BaseModel


class ProductBase(SQLModel):
    name: str = Field(nullable=False)
    price: float = Field(nullable=False)
    description: str | None = Field(nullable=True)
#

class Product(ProductBase, BaseModel, table=True):
    pass
