from sqlalchemy.ext.asyncio import AsyncSession

from src.tanks.model import Branch, BranchType, Tank


async def fill_database_utils(session: AsyncSession):
    branch1: Branch = Branch(id=1, name="Concept", type=BranchType.CT, comfort=5)
    branch2: Branch = Branch(id=2, name="Controcarro 3 Minotauro", type=BranchType.PT, comfort=5)
    branch3: Branch = Branch(id=3, name="Объект 705А ", type=BranchType.TT, comfort=5)

    tank1: Tank = Tank(
        name="Tank 1",
        branch_id=1,
        level=6, price=1_000_0003,
        exp_cost=50_000,
        available=False,
        battle_experience=0,
        pass_free = True,
    )

    tank2: Tank = Tank(
        name="Tank 2",
        branch_id=1,
        level=7, price=2_000_000,
        exp_cost=70_000,
        available=False,
        battle_experience=0,
        pass_free=True,
    )

    tank3: Tank = Tank(
        name="Tank 3",
        branch_id=1,
        level=8, price=3_000_000,
        exp_cost=100_000,
        available=True,
        battle_experience=0,
    )

    tank4: Tank = Tank(
        name="Tank 4",
        branch_id=1,
        level=9, price=4_000_000,
        exp_cost=150_000,
        available=True,
        battle_experience=0
    )

    tank5: Tank = Tank(
        name="Tank 5",
        branch_id=1,
        level=10, price=6_100_000,
        exp_cost=0,
        available=False,
        battle_experience=0
    )

    tank2_1: Tank = Tank(name="Tank 1", branch_id=2,level=6, price=890_000, exp_cost=28_500, available=False, battle_experience=0)
    tank2_2: Tank = Tank(name="SMV CC-56", branch_id=2,level=7, price=1_370_000, exp_cost=46_300, available=False, battle_experience=0)
    tank2_3: Tank = Tank(name="SMV CC-67", branch_id=2,level=8, price=2_530_000, exp_cost=73_900, available=True, battle_experience=154_100)
    tank2_4: Tank = Tank(name="Controcarro 1 Mk.", branch_id=2,level=9, price=3_550_000, exp_cost=154_100, available=True, battle_experience=380_000)
    tank2_5: Tank = Tank(name="Minotauro", branch_id=2,level=10, price=6_100_000, exp_cost=197_400, available=False, battle_experience=0)

    tank3_1: Tank = Tank(name="КВ-1С", branch_id=3,level=6, price= 910_000, exp_cost=25_650, available=False, battle_experience=0)
    tank3_2: Tank = Tank(name="ИС", branch_id=3,level=7, price=1_424_000, exp_cost=49_480, available=False, battle_experience=0)
    tank3_3: Tank = Tank(name="ИС-М", branch_id=3,level=8, price=2_550_000, exp_cost=58_000, available=True, battle_experience=154_100)
    tank3_4: Tank = Tank(name="Объект 705", branch_id=3,level=9, price=3_570_000, exp_cost=144_900, available=True, battle_experience=380_000)
    tank3_5: Tank = Tank(name="Объект 705А", branch_id=3,level=10, price=6_100_000, exp_cost=162_300, available=False, battle_experience=0)

    session.add_all([branch1, tank1, tank2, tank3, tank4, tank5])
    session.add_all([branch2, tank2_1, tank2_2, tank2_3, tank2_4, tank2_5])
    session.add_all([branch3, tank3_1, tank3_2, tank3_3, tank3_4, tank3_5])
    await session.commit()
