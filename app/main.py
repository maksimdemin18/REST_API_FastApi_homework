from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Advertisement Service",
    description="Сервис объявлений купли/продажи",
    version="1.0.0",
)


@app.post(
    "/advertisement",
    response_model=schemas.AdvertisementResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создать объявление",
)
def create_advertisement(
    advertisement_data: schemas.AdvertisementCreate,
    db: Session = Depends(get_db),
):
    return crud.create_advertisement(db, advertisement_data)


@app.get(
    "/advertisement",
    response_model=list[schemas.AdvertisementResponse],
    summary="Поиск объявлений",
)
def search_advertisements(
    title: Optional[str] = None,
    description: Optional[str] = None,
    author: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Session = Depends(get_db),
):
    return crud.search_advertisements(
        db=db,
        title=title,
        description=description,
        author=author,
        min_price=min_price,
        max_price=max_price,
    )


@app.get(
    "/advertisement/{advertisement_id}",
    response_model=schemas.AdvertisementResponse,
    summary="Получить объявление по id",
)
def get_advertisement(
    advertisement_id: int,
    db: Session = Depends(get_db),
):
    advertisement = crud.get_advertisement_by_id(db, advertisement_id)
    if advertisement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Advertisement not found",
        )
    return advertisement


@app.patch(
    "/advertisement/{advertisement_id}",
    response_model=schemas.AdvertisementResponse,
    summary="Обновить объявление",
)
def update_advertisement(
    advertisement_id: int,
    update_data: schemas.AdvertisementUpdate,
    db: Session = Depends(get_db),
):
    advertisement = crud.get_advertisement_by_id(db, advertisement_id)
    if advertisement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Advertisement not found",
        )

    return crud.update_advertisement(db, advertisement, update_data)


@app.delete(
    "/advertisement/{advertisement_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить объявление",
)
def delete_advertisement(
    advertisement_id: int,
    db: Session = Depends(get_db),
):
    advertisement = crud.get_advertisement_by_id(db, advertisement_id)
    if advertisement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Advertisement not found",
        )

    crud.delete_advertisement(db, advertisement)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
