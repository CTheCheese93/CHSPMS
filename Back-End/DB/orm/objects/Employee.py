import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedAsDataclass
from typing import Optional, List

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class Employee(MappedAsDataclass, Base):
    __tablename__ = "employee"

    id: Mapped[str] = mapped_column(primary_key=True, default_factory=getUUID, init=False)
    employee_id: Mapped[Optional[int]] = mapped_column(unique=True, init=False)
    first_name: Mapped[int]
    last_name: Mapped[int]
    first_hire_date: Mapped[Optional[datetime]] = mapped_column(init=False)
    most_recent_hire_date: Mapped[Optional[datetime]] = mapped_column(init=False)

    manager_id: Mapped[Optional[str]] = mapped_column(ForeignKey("employee.id"), init=False)

    manager: Mapped[Optional["Employee"]] = relationship(back_populates="employees", remote_side=id, default=None)
    employees: Mapped[Optional[List["Employee"]]] = relationship(back_populates="manager", init=False, repr=False)

    injuries_had: Mapped[List["Injury"]] = relationship(
        back_populates="employee", init=False,
        primaryjoin="Employee.id==Injury.employee_dbid"
    )

    injuries_managed: Mapped[List["Injury"]] = relationship(
        back_populates="manager", init=False,
        primaryjoin="Employee.id==Injury.manager_dbid"
    )

    def __repr__(self) -> str:
        return generate_repr("Employee", {
            "id": self.id,
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "first_hire_date": self.first_hire_date,
            "most_recent_hire_date": self.most_recent_hire_date
        })