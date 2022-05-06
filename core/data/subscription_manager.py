import json
from dataclasses import dataclass
from typing import List


@dataclass
class Subscription:
    id: str
    districts: List[int]
    price_min: int
    price_max: int

    def update(self, new):
        for key, value in new.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self


class SubscriptionManager:
    def __init__(self, path: str):
        self._path = path

    def subscriptions(self) -> List[Subscription]:
        try:
            with open(self._path, "r") as db:
                now = json.loads(db.read())
                return list(map(lambda m: Subscription(**m), now))
        except Exception:
            return []

    def add(self, subscription: Subscription):
        subscriptions = self.subscriptions()
        for s in subscriptions:
            if s.id == subscription.id:
                subscriptions.remove(s)

        if subscription not in subscriptions:
            with open(self._path, "w") as db:
                subscriptions.append(subscription)
                json.dump(subscriptions, db, default=vars)

    def get(self, id: str) -> Subscription:
        return next(subscription for subscription in self.subscriptions() if subscription.id == str(id))

    def update(self, id: str, fields):
        self.add(self.get(id).update(fields))

    def register(self, id: str):
        self.add(Subscription(id, [], 0, 3200))
