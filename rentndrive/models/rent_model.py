from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import DATE
from .base_model import BaseModel
from common.enum.status import Status


class RentModel(BaseModel):
    __tablename__ = "rents"

    rent_id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
    status: Mapped[Status] = mapped_column(nullable=False)
    starts_at: Mapped[DATE] = mapped_column(nullable=False)
    ends_at: Mapped[DATE] = mapped_column(nullable=False)





