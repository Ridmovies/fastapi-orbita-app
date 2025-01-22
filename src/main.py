from fastapi import FastAPI

from src.dev.router import router as dev_router

app = FastAPI()
app.include_router(dev_router, prefix='/dev', tags=['dev'])
