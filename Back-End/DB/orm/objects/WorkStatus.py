import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class WorkStatus(Base):
    __tablename__ = "work_status"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    status: Mapped[str]

    employees: Mapped[List["Employee"]] = relationship(
        back_populates="work_status",
        primaryjoin="WorkStatus.id==Employee.work_status_id"
    )

    def __repr__(self) -> str:
        return generate_repr("WorkStatus", {
            "id": self.id,
            "title": self.status
        })