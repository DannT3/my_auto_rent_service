from sqlalchemy.orm import Mapped, mapped_column
from .base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    surname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column()