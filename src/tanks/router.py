from fastapi import APIRouter

from src.database import SessionDep
from src.tanks.service import TankService

tank_router = APIRouter()

@tank_router.get("")
async def get_tanks():
    return await TankService.get_all()


@tank_router.get("/branch/{branch_id}/total_cost")
async def get_calculate_branch(session: SessionDep, branch_id: int):
    return await TankService.get_calc_total_cost(session=session, branch_id=branch_id)

@tank_router.get("/branch/{branch_id}/calculate")
async def get_calculate_branch(session: SessionDep, branch_id: int):
    return await TankService.get_calc_branch(session=session, branch_id=branch_id)


@tank_router.get("/branch/calc_all")
async def get_calculate_branch(session: SessionDep):
    return await TankService.calc_all(session=session)