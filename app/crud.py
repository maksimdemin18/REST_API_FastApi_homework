from typing import Optional

from sqlalchemy.orm import Session

from app import models, schemas


def create_advertisement(db: Session, advertisement_data: schemas.AdvertisementCreate) -> models.Advertisement:
    advertisement = models.Advertisement(**advertisement_data.model_dump())
    db.add(advertisement)
    db.commit()
    db.refresh(advertisement)
    return advertisement


def get_advertisement_by_id(db: Session, advertisement_id: int) -> Optional[models.Advertisement]:
    return (
        db.query(models.Advertisement)
        .filter(models.Advertisement.id == advertisement_id)
        .first()
    )


def update_advertisement(
    db: Session,
    advertisement: models.Advertisement,
    update_data: schemas.AdvertisementUpdate,
) -> models.Advertisement:
    values = update_data.model_dump(exclude_unset=True)

    for field_name, field_value in values.items():
        setattr(advertisement, field_name, field_value)

    db.commit()
    db.refresh(advertisement)
    return advertisement


def delete_advertisement(db: Session, advertisement: models.Advertisement) -> None:
    db.delete(advertisement)
    db.commit()


def search_advertisements(
    db: Session,
    title: Optional[str] = None,
    description: Optional[str] = None,
    author: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
):
    query = db.query(models.Advertisement)

    if title:
        query = query.filter(models.Advertisement.title.ilike(f"%{title}%"))

    if description:
        query = query.filter(models.Advertisement.description.ilike(f"%{description}%"))

    if author:
        query = query.filter(models.Advertisement.author.ilike(f"%{author}%"))

    if min_price is not None:
        query = query.filter(models.Advertisement.price >= min_price)

    if max_price is not None:
        query = query.filter(models.Advertisement.price <= max_price)

    return query.order_by(models.Advertisement.id.asc()).all()
