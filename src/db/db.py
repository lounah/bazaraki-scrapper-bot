from abc import ABC, abstractmethod
from tinydb import TinyDB


class Database(ABC):
    def __init__(self, path: str):
        self._db = TinyDB(path)

    @abstractmethod
    def add(self, obj):
        ...

    @abstractmethod
    def add_all(self, obj):
        ...

    @abstractmethod
    def remove(self, id):
        ...

    @abstractmethod
    def get(self, id):
        ...

    @abstractmethod
    def all(self):
        ...
