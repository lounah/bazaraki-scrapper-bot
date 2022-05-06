import re
from typing import List

from bs4 import BeautifulSoup

from core.data.estate import Estate


class EstateMapper:

    def map(self, html: str) -> List[Estate]:
        _soup = BeautifulSoup(html, 'html.parser')
        _announcements = _soup.body.find_all('li', attrs={'class': 'announcement-container'})
        return list(map(self._as_estate, _announcements))

    def _as_estate(self, announcement) -> Estate:
        _url = self._extract_url(announcement)
        return Estate(
            date=self._extract_date(announcement),
            description=self._extract_description(announcement),
            id=re.search("/adv/(\d+)_", _url).group(1),
            location=self._extract_location(announcement),
            price=self._extract_price(announcement),
            title=self._extract_title(announcement),
            url=f"www.bazaraki.com{_url}"
        )

    @staticmethod
    def _extract_url(announcement) -> str:
        return announcement.find("a", attrs={"class": "mask"}).get("href")

    @staticmethod
    def _extract_price(announcement) -> str:
        return announcement.find("meta", attrs={"itemprop": "price"}).get("content")

    @staticmethod
    def _extract_title(announcement) -> str:
        return announcement.find("meta", attrs={"itemprop": "name"}).get("content").strip()

    @staticmethod
    def _extract_location(announcement) -> str:
        return announcement.find("meta", attrs={"itemprop": "areaServed"}).get("content")

    @staticmethod
    def _extract_description(announcement) -> str:
        try:
            return announcement \
                .find("div", attrs={"class": "announcement-block-text announcement-block__text"}) \
                .find("div", attrs={"class": "announcement-block-text-container announcement-block__text-container"}) \
                .find("div", attrs={"class": "announcement-block__description"}).text
        except AttributeError:
            return ""

    @staticmethod
    def _extract_date(announcement) -> str:
        try:
            date = announcement \
                .find("div", attrs={"class": "announcement-block-text announcement-block__text"}) \
                .find("div", attrs={"class": "announcement-block-text-container announcement-block__text-container"}) \
                .find("div", attrs={"class": "announcement-block__date"}).text
            return re.search("(\d+)[.](\d+)[.](\d+).(\d+:\d+)|\w+.(\d+:\d+)", date).group(0)
        except AttributeError:
            return ""
