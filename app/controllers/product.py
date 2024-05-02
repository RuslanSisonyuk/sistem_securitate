from fastapi import APIRouter, Depends

from app.repositories.product import ProductRepository
from app.schemas.product import ProductRead

product_router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@product_router.get(
    "/",
    summary="Get all products.",
    response_model=list[ProductRead],
)
async def get_products(product_repository: ProductRepository = Depends(ProductRepository)) -> list[ProductRead]:
    return product_repository.get_all()
