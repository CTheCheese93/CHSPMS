import sys

sys.path.append('E:\Programming\projects\CHSPMS\Back-End\DB')

from sqlalchemy.orm import Mapped, mapped_column

from helpers.uuid_helpers import getUUID
from helpers.generate_repr import generate_repr
from .Base import Base

class SWMType(Base):
    __tablename__ = "swm_type"

    id: Mapped[str] = mapped_column(primary_key=True, default=getUUID)
    name: Mapped[str]
    

    def __repr__(self) -> str:
        return generate_repr("SWMType", {
            "id": self.id,
            "name": self.name
        })