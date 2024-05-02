from app.core.repository import Repository, Model

Product = dict


@Model(Product)
class ProductRepository(Repository):
    pass
