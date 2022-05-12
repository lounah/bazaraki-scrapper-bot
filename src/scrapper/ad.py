from dataclasses import dataclass
from enum import Enum

from src.api.district import District
from src.bot.subscriptions import Subscription


class Category(str, Enum):
    ESTATE = 0
    CARS = 1


@dataclass
class Ad:
    category: Category
    date: str
    description: str
    id: str
    location: str
    price: str
    title: str
    url: str

    def __str__(self) -> str:
        return (
            f'💶 <strong>{int(float(self.price))} €</strong>\n'
            f'📝 <strong>{self.title}</strong>\n'
            f'🗺️ <strong>{self.location}</strong>\n'
            f'📅 <strong>{self.date}</strong>\n'
            f'<a href="{self.url}">Link</a>'
        )

    def district(self) -> District:
        if "Paphos" in self.location:
            return District.PAPHOS
        elif "Famagusta" in self.location:
            return District.FAMAGUSTA
        elif "Larnaka" in self.location:
            return District.LARNACA
        elif "Lefkosia" in self.location:
            return District.LEFKOSIA
        elif "Limassol" in self.location:
            return District.LIMASSOL
        else:
            return District.UNKNOWN

    def matches_subscription(self, subscription: Subscription) -> bool:
        price = int(float(self.price))
        district = self.district().value

        matches_car = price in range(subscription.car.price_min, subscription.car.price_max) and district == subscription.car.district
        marches_estate = price in range(subscription.estate.price_min, subscription.estate.price_max) and district == subscription.estate.district

        return matches_car or marches_estate
