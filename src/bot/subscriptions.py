from pydantic import BaseModel

from src.api.district import District


class CarSubscription(BaseModel):
    district: int
    query: str
    price_min: int
    price_max: int

    def __str__(self):
        if self.district == District.UNKNOWN.value:
            return (
                f'🚗️ <strong>Car</strong>\n'
                f'No filters.\n'
            )
        else:
            return (
                f'🚗️ <strong>Car</strong>\n'
                f'💶 <strong>{int(float(self.price_min))} - {int(float(self.price_max))} €</strong>\n'
                f'📝 {self.query}\n'
                f'🗺️ {District(int(self.district)).name.title()}\n'
            )


class EstateSubscription(BaseModel):
    district: int
    price_min: int
    price_max: int

    def __str__(self):
        if self.district == District.UNKNOWN.value:
            return (
                f'🏘️️ <strong>House</strong>\n'
                f'No filters.\n'
            )
        else:
            return (
                f'🏘️️ <strong>House</strong>\n'
                f'💶 <strong>{int(float(self.price_min))} - {int(float(self.price_max))} €</strong>\n'
                f'🗺️ {District(int(self.district)).name.title()}\n'
            )


class Subscription(BaseModel):
    id: str
    car: CarSubscription
    estate: EstateSubscription

    @staticmethod
    def new(id: str):
        return Subscription(
            id=id,
            car=CarSubscription(
                district=District.UNKNOWN.value,
                query="",
                price_min=0,
                price_max=0
            ),
            estate=EstateSubscription(
                district=District.UNKNOWN.value,
                price_min=0,
                price_max=0
            )
        )

    def __str__(self):
        if not self.car and not self.estate:
            return "You ain't got no search filters. Start getting notifications via /start command."
        else:
            return (
                f'{str(self.car)}\n'
                f'{str(self.estate)}\n'
            )


# https://github.com/msiemens/tinydb/issues/274
def set_nested(path, val):
    def transform(doc):
        current = doc
        for key in path[:-1]:
            current = current[key]

        current[path[-1]] = val

    return transform
