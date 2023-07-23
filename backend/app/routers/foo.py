from typing import List

from fastapi import APIRouter, Depends

from app.config.database import get_db
from app.schemas.foo import FooItem, FooItemCreate
from app.services.foo import FooService
from app.utils.service_result import handle_result

router = APIRouter()


@router.post("/item/", response_model=FooItem)
def create_item(item: FooItemCreate, db: get_db = Depends()):
    result = FooService(db).create_item(item)
    return handle_result(result)


@router.get("/item/{item_id}", response_model=FooItem)
def get_item(item_id: int, db: get_db = Depends()):
    result = FooService(db).get_item(item_id)
    return handle_result(result)


@router.get("/all_items/", response_model=List[FooItem])
def get_all_items(db: get_db = Depends()):
    result = FooService(db).get_all_items()
    return handle_result(result)


@router.delete("/item/{item_id}", response_model=int)
def delete_item(item_id: int, db: get_db = Depends()):
    result = FooService(db).delete_item(item_id)
    return handle_result(result)
