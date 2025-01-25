from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin

from src.admin.views import TankAdmin, BranchAdmin
from src.database import engine
from src.dev.router import router as dev_router
from src.tanks.router import tank_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    yield

app = FastAPI(lifespan=lifespan)
admin = Admin(app, engine)
admin.add_view(TankAdmin)
admin.add_view(BranchAdmin)

app.include_router(dev_router, prefix='/dev', tags=['dev'])
app.include_router(tank_router, prefix='/tanks', tags=['tanks'])

