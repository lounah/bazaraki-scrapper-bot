from dataclasses import asdict
from typing import Optional, List

from tinydb import Query
from tinydb.table import Document

from db.db import Database
from scrapper.ad import Ad


class AdsDatabase(Database):
    def __init__(self, path: str):
        super().__init__(path)
        self._table = self._db.table('ads')

    def add(self, ad: Ad):
        self._table.insert(asdict(ad), doc_id=ad.id)

    def add_all(self, obj: List[Ad]):
        insertions = list(map(lambda ad: Document(asdict(ad), doc_id=ad.id), obj))
        for doc in insertions:
            self._table.upsert(doc)

    def remove(self, id: str):
        self._table.remove(Query().id == id)

    def get(self, id: str) -> Optional[Ad]:
        return self._table.get(Query().id == id)

    def all(self) -> List[Ad]:
        return list(map(lambda ad: Ad(**ad), self._table.all()))
