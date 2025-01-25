from sqlalchemy import select
from sqlalchemy.sql.functions import func
from sqlalchemy.ext.asyncio import AsyncSession
from src.services import BaseService
from src.tanks.model import Tank, Branch


class TankService(BaseService):
    model = Tank

    @classmethod
    async def get_calc_total_cost(cls, session: AsyncSession, branch_id: int):
        query = select(func.sum(Tank.price)).where(Tank.branch_id == branch_id)
        result = await session.execute(query)
        total_cost = result.scalar_one()
        return total_cost

    @classmethod
    async def get_calc_branch(cls, session: AsyncSession, branch_id: int):
        query = select(Tank).where(Tank.branch_id == branch_id)
        result = await session.execute(query)
        tanks = result.scalars().all()
        total_cost = 0
        extra_cost = 0
        total_exp = 0
        need_free_exp = 0

        for tank in tanks:
            # COST
            if tank.available:
                total_cost += int(tank.price / 2)
                extra_cost += int(tank.price / 2)
            else:
                total_cost += tank.price


            if tank.pass_free:
                need_free_exp += tank.exp_to_next

            # EXP
            total_exp += tank.exp_to_next

        return {
            "branch_id": branch_id,
            "total_cost": total_cost,
            "extra_cost": extra_cost,
            "total_exp": total_exp,
            "need_free_exp": need_free_exp,
        }

    @classmethod
    async def calc_all(cls, session: AsyncSession):
        query = select(Branch)
        result = await session.execute(query)
        branches = result.scalars().all()

        stat_branches = []
        for branch in branches:
            stat_branches.append(await cls.get_calc_branch(session=session, branch_id=branch.id))

        return stat_branches


