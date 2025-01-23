from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.dev.router import router as dev_router
from src.posts.router import router as post_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(dev_router, prefix='/dev', tags=['dev'])
app.include_router(post_router, prefix='/posts', tags=['posts'])
