from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AdvertisementCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Заголовок объявления")
    description: str = Field(..., min_length=1, description="Описание объявления")
    price: float = Field(..., ge=0, description="Цена")
    author: str = Field(..., min_length=1, max_length=255, description="Автор объявления")


class AdvertisementUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, ge=0)
    author: Optional[str] = Field(None, min_length=1, max_length=255)


class AdvertisementResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    author: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
