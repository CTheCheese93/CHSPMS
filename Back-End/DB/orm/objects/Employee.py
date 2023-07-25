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
    
    job_class_id: Mapped[Optional[str]] = mapped_column(ForeignKey("job_class.id"), init=False)
    job_class: Mapped[Optional["JobClass"]] = relationship(
        back_populates="employees", foreign_keys=[job_class_id], init=False,
        primaryjoin="Employee.job_class_id==JobClass.id"
    )

    manager_id: Mapped[Optional[str]] = mapped_column(ForeignKey("employee.id"), init=False)
    manager: Mapped[Optional["Employee"]] = relationship(back_populates="employees", remote_side=id, default=None)
    
    primary_department_id: Mapped[Optional[str]] = mapped_column(ForeignKey("primary_department.id"), init=False)
    primary_department: Mapped[Optional["PrimaryDepartment"]] = relationship(
        back_populates="employees", foreign_keys=[primary_department_id], init=False,
        primaryjoin="Employee.primary_department_id==PrimaryDepartment.id")

    secondary_department_id: Mapped[Optional[str]] = mapped_column(ForeignKey("secondary_department.id"), init=False)
    secondary_department: Mapped[Optional["SecondaryDepartment"]] = relationship(
        back_populates="employees", foreign_keys=[secondary_department_id], init=False,
        primaryjoin="Employee.secondary_department_id==SecondaryDepartment.id")

    work_status_id: Mapped[Optional[str]] = mapped_column(ForeignKey("work_status.id"), init=False)
    work_status: Mapped[Optional["WorkStatus"]] = relationship(
        back_populates="employees", foreign_keys=[work_status_id], init=False,
        primaryjoin="Employee.work_status_id==WorkStatus.id"
    )

    injuries_had: Mapped[List["Injury"]] = relationship(
        back_populates="employee", init=False,
        primaryjoin="Employee.id==Injury.employee_dbid"
    )


    # Specific to full time employees

    employees: Mapped[Optional[List["Employee"]]] = relationship(back_populates="manager", init=False, repr=False)

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