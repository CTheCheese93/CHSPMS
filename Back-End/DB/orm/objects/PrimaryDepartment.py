import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from sqlalchemy.orm import Mapped, mapped_column

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from objects.Base import Base

class PrimaryDepartment(Base):
    __tablename__ = "primary_department"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    name: Mapped[str]

    def __repr__(self) -> str:
        return generate_repr("PrimaryDepartment", {
            "id": self.id,
            "name": self.name
        })