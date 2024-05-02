from fastapi import FastAPI

from app.controllers.product import product_router
from app.core.database import init_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(product_router)

