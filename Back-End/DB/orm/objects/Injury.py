import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class Injury(Base):
    __tablename__ = "injury"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    employee_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    manager_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    injury_date: Mapped[Optional[datetime]]

    employee: Mapped["Employee"] = relationship(foreign_keys=employee_dbid)
    manager: Mapped["Employee"] = relationship(foreign_keys=manager_dbid)

    def __repr__(self) -> str:
        return generate_repr("Injury", {
            "id": self.id,
            "employee_dbid": self.employee_dbid,
            "manager_dbid": self.manager_dbid,
            "injury_date": self.injury_date
        })