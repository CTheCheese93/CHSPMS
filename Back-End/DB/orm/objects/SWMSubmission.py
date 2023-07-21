import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class SWMSubmission(Base):
    __tablename__ = "swm_submission"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    swm_type: Mapped[str] = mapped_column(ForeignKey("swm_type.id"))
    employee_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    trainer_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    manager_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    submission_date: Mapped[Optional[datetime]]

    def __repr__(self) -> str:
        return generate_repr("SWMSubmission", {
            "id": self.id,
            "swm_type": self.swm_type,
            "employee_dbid": self.employee_dbid,
            "trainer_dbid": self.trainer_dbid,
            "manager_dbid": self.manager_dbid_dbid,
            "submission_date": self.submission_date
        })