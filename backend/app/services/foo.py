from typing import Optional, List

from app.models.foo import FooItem
from app.schemas.foo import FooItemCreate
from app.services.main import AppService, AppCRUD
from app.utils.app_exceptions import AppException
from app.utils.service_result import ServiceResult


class FooService(AppService):
    def create_item(self, item: FooItemCreate) -> ServiceResult:
        foo_item = FooCRUD(self.db).create_item(item)
        if not foo_item:
            return ServiceResult(AppException.FooCreateItem())
        return ServiceResult(foo_item)

    def get_item(self, item_id: int) -> ServiceResult:
        foo_item = FooCRUD(self.db).get_item(item_id)
        if not foo_item:
            return ServiceResult(AppException.FooGetItem({"item_id": item_id}))
        if not foo_item.public:
            return ServiceResult(AppException.FooItemRequiresAuth())
        return ServiceResult(foo_item)

    def get_all_items(self) -> ServiceResult:
        foo_items = FooCRUD(self.db).get_all_items()
        return ServiceResult(foo_items)

    def delete_item(self, item_id: int) -> ServiceResult:
        foo_item_id: int = FooCRUD(self.db).delete_item(item_id)
        if foo_item_id is None:
            return ServiceResult(AppException.FooGetItem({"item_id": item_id}))
        return ServiceResult(foo_item_id)


class FooCRUD(AppCRUD):
    def create_item(self, item: FooItemCreate) -> FooItem:
        foo_item = FooItem(description=item.description, public=item.public)
        self.db.add(foo_item)
        self.db.commit()
        self.db.refresh(foo_item)
        return foo_item

    def get_item(self, item_id: int) -> Optional[FooItem]:
        foo_item = self.db.query(FooItem).filter(FooItem.id == item_id).first()
        if foo_item:
            return foo_item
        return None

    def get_all_items(self) -> Optional[List[FooItem]]:
        foo_items = self.db.query(FooItem).all()
        return foo_items

    def delete_item(self, item_id: int) -> Optional[int]:
        foo_item = self.db.query(FooItem).filter(FooItem.id == item_id).first()
        if foo_item:
            self.db.delete(foo_item)
            self.db.commit()
            return item_id
        else:
            return None
