import json
from json import JSONDecodeError
from typing import List

from core.data.estate import Estate


class EstateDatabase:
    def __init__(self, storage_path: str):
        self._path = storage_path

    def add_all(self, estates: List[Estate]):
        now = self.get_all()
        with open(self._path, "w") as db:
            json.dump(now + estates, db, default=vars)

    def get_all(self) -> List[Estate]:
        try:
            with open(self._path, "r") as db:
                now = json.loads(db.read())
                return list(map(lambda m: Estate(**m), now))
        except JSONDecodeError:
            return []
