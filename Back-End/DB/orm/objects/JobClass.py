import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class JobClass(Base):
    __tablename__ = "job_class"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    title: Mapped[str]
    code: Mapped[str]

    employees: Mapped[List["Employee"]] = relationship(back_populates="job_class",
        primaryjoin="JobClass.id==Employee.job_class_id"
    )

    def __repr__(self) -> str:
        return generate_repr("JobClass", {
            "id": self.id,
            "title": self.title,
            "code": self.code
        })