from typing import List

from tinydb import Query
from tinydb.table import Document

from src.bot.subscriptions import Subscription, set_nested
from src.db.db import Database


class SubscriptionsDatabase(Database):
    def __init__(self, path: str):
        super().__init__(path)
        self._table = self._db.table('subscriptions')

    def add(self, subscription: Subscription):
        if not self.get(subscription.id):
            self._table.upsert(Document(subscription.dict(), doc_id=int(subscription.id)))

    def add_all(self, obj):
        insertions = list(map(lambda sub: Document(sub.dict(), doc_id=sub.id), obj))
        self._table.update_multiple(insertions)

    def remove(self, id: str):
        self._table.remove(Query().id == id)

    def get(self, id: str) -> Subscription:
        fields = self._table.get(Query().id == str(id))
        return Subscription(**fields) if fields else None

    def update(self, id: str, path, val):
        self._table.update(set_nested(path, val), Query().id == id)

    def all(self) -> List[Subscription]:
        return list(map(lambda sub: Subscription(**sub), self._table.all()))
