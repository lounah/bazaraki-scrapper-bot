from enum import Enum


class District(Enum):
    FAMAGUSTA = 8
    LARNACA = 10
    LEFKOSIA = 11
    LIMASSOL = 12
    PAPHOS = 13

    @staticmethod
    def values():
        return [e.value for e in District]
