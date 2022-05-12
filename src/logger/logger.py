import os
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    VERBOSE = 2
    ERROR = 3


class Logger(ABC):

    @abstractmethod
    def debug(self, msg: str):
        ...

    @abstractmethod
    def info(self, msg: str):
        ...

    @abstractmethod
    def verbose(self, msg: str):
        ...

    @abstractmethod
    def error(self, msg: str):
        ...


class LogTarget(ABC):

    @abstractmethod
    def write(self, level: LogLevel, msg: str):
        ...


class FileTarget(LogTarget):
    def __init__(self, path: str):
        self._path = path

    def write(self, level: LogLevel, msg: str):
        with open(self._path, 'a') as output:
            time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
            output.write(f'{time} [{level.name}] {msg}\n')


class SystemOutTarget(LogTarget):

    def write(self, level: LogLevel, msg: str):
        time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        print(f'{time} [{level.name}] {msg}\n')


class LoggerImpl(Logger):
    def __init__(self, targets: [LogTarget]):
        self._targets = targets

    def debug(self, msg: str):
        for target in self._targets:
            target.write(LogLevel.DEBUG, msg)

    def info(self, msg: str):
        for target in self._targets:
            target.write(LogLevel.INFO, msg)

    def verbose(self, msg: str):
        for target in self._targets:
            target.write(LogLevel.VERBOSE, msg)

    def error(self, msg: str):
        for target in self._targets:
            target.write(LogLevel.ERROR, msg)
