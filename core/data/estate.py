from dataclasses import dataclass
from core.data.district import District


@dataclass
class Estate:
    date: str
    description: str
    id: str
    location: str
    price: str
    title: str
    url: str

    def telegram_msg(self) -> str:
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
            return District.LIMASSOL
