from sqlalchemy.orm import Mapped, mapped_column
from .base_model import BaseModel
from common.enum.car_type import CarType


class CarModel(BaseModel):
    __tablename__ = "Cars"    

    car_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    mileage: Mapped[int] = mapped_column(nullable=False)
    car_type: Mapped["CarType"] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Car id:{CarModel.car_id}, car brand: {CarModel.brand}, car price: {CarModel.price}, car type: {CarModel.car_type}"






