from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.controllers.quiz import router as homepage_router

app = FastAPI()
app.include_router(homepage_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
