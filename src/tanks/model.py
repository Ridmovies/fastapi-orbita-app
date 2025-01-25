from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base


# Определяем перечисление для типов веток
class BranchType(Enum):
    CT = 'CT'
    TT = 'TT'
    PT = 'PT'
    LT = 'LT'


class Branch(Base):
    name: Mapped[str]
    type: Mapped[BranchType] = mapped_column(default=BranchType.CT)
    comfort: Mapped[int] = mapped_column(default=5)

    tanks: Mapped[list["Tank"]] = relationship(back_populates="branch")

    def __repr__(self):
        return f"Branch(name={self.name}, type={self.type})"

class Tank(Base):
    name: Mapped[str]
    level: Mapped[int] = mapped_column(default=6)
    price: Mapped[int] = mapped_column(default=0)
    exp_to_next: Mapped[int] = mapped_column(default=0)
    available: Mapped[bool] = mapped_column(default=True)
    pass_free: Mapped[bool] = mapped_column(default=False)
    battle_experience: Mapped[int] = mapped_column(default=0)
    bon_equipment: Mapped[int] = mapped_column(default=0)

    branch_id: Mapped[int] = mapped_column(ForeignKey("branch.id"), default=1)
    branch: Mapped["Branch"] = relationship(back_populates="tanks")

    def __repr__(self):
        return f"Tank(name={self.name}, branch_id={self.branch_id})"
