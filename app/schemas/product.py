from datetime import datetime

from app.models.product import ProductBase


class ProductRead(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ProductCreate(ProductBase):
    pass
