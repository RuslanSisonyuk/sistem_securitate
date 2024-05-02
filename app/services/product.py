from fastapi import Depends

from app.repositories.product import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository = Depends(ProductRepository)):
        self.product_repository = product_repository

    def create_product(self, data):
        return self.product_repository.create(data)
