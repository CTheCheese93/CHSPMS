import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class SWMSubmission(MappedAsDataclass, Base):
    __tablename__ = "swm_submission"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID, init=False)
    is_rostered: Mapped[bool] = mapped_column(default=False, init=False)
    
    swm_type_id: Mapped[str] = mapped_column(ForeignKey("swm_type.id"))
    swm_type: Mapped["SWMType"] = relationship(
        back_populates="swm_submissions", foreign_keys=[swm_type_id],
        primaryjoin="SWMSubmission.swm_type_id==SWMType.id"
    )
    
    employee_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    employee: Mapped["Employee"] = relationship(
        back_populates="swms_had", foreign_keys=[employee_dbid],
        primaryjoin="SWMSubmission.employee_dbid==Employee.id"
    )

    trainer_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"))
    trainer: Mapped["Employee"] = relationship(
        back_populates="swms_performed", foreign_keys=[trainer_dbid],
        primaryjoin="SWMSubmission.trainer_dbid==Employee.id"
    )

    manager_dbid: Mapped[str] = mapped_column(ForeignKey("employee.id"), default=None, init=False)
    manager: Mapped["Employee"] = relationship(
        back_populates="swms_managed", foreign_keys=[manager_dbid],
        primaryjoin="SWMSubmission.manager_dbid==Employee.id"
    )

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