from sqlalchemy.ext.asyncio import AsyncSession

from src.tanks.model import Branch, BranchType, Tank


async def fill_database_utils(session: AsyncSession):
    branch1: Branch = Branch(id=1, name="Concept", type=BranchType.CT, comfort=5)
    branch2: Branch = Branch(id=2, name="Branch 2", type=BranchType.CT, comfort=5)

    tank1: Tank = Tank(
        name="Tank 1",
        branch_id=1,
        level=6, price=1_000_000,
        exp_to_next=50_000,
        available=False,
        battle_experience=0,
        pass_free = True,
    )

    tank2: Tank = Tank(
        name="Tank 2",
        branch_id=1,
        level=7, price=2_000_000,
        exp_to_next=70_000,
        available=False,
        battle_experience=0,
        pass_free=True,
    )

    tank3: Tank = Tank(
        name="Tank 3",
        branch_id=1,
        level=8, price=3_000_000,
        exp_to_next=100_000,
        available=True,
        battle_experience=0,
    )

    tank4: Tank = Tank(
        name="Tank 4",
        branch_id=1,
        level=9, price=4_000_000,
        exp_to_next=150_000,
        available=True,
        battle_experience=0
    )

    tank5: Tank = Tank(
        name="Tank 5",
        branch_id=1,
        level=10, price=6_000_000,
        exp_to_next=0,
        available=False,
        battle_experience=0
    )

    tank2_1: Tank = Tank(name="Tank 1", branch_id=2,level=6, price=100, exp_to_next=None, available=True, battle_experience=0)
    tank2_2: Tank = Tank(name="Tank 1", branch_id=2,level=7, price=100, exp_to_next=None, available=True, battle_experience=0)
    tank2_3: Tank = Tank(name="Tank 1", branch_id=2,level=8, price=100, exp_to_next=None, available=True, battle_experience=0)
    tank2_4: Tank = Tank(name="Tank 1", branch_id=2,level=9, price=100, exp_to_next=None, available=True, battle_experience=0)
    tank2_5: Tank = Tank(name="Tank 1", branch_id=2,level=10, price=100, exp_to_next=None, available=True, battle_experience=0)

    session.add_all([branch1, branch2])
    session.add_all([tank1, tank2, tank3, tank4, tank5])
    session.add_all([tank2_1, tank2_2, tank2_3, tank2_4, tank2_5])
    await session.commit()
