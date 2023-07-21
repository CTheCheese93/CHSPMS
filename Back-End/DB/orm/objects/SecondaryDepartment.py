import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class SecondaryDepartment(Base):
    __tablename__ = "secondary_department"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    name: Mapped[str]
    primary_department: Mapped[str] = mapped_column(ForeignKey("primary_department.id"))


    def __repr__(self) -> str:
        return generate_repr("SecondaryDepartment", {
            "id": self.id,
            "name": self.name,
            "primary_department_dbid": self.primary_department
        })