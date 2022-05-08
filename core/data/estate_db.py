import json
from json import JSONDecodeError
from typing import List


class EstateDatabase:
    def __init__(self, storage_path: str):
        self._path = storage_path

    def add_all(self, estates: List[str]):
        now = self.get_all()
        with open(self._path, "w") as db:
            json.dump(now + estates, db, default=vars)

    def get_all(self) -> List[str]:
        try:
            with open(self._path, "r") as db:
                return list(json.loads(db.read()))
        except JSONDecodeError:
            return []
