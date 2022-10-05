from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional
from enum import Enum

class DataType(Enum):
    STR = 'string'
    INT = 'integer'
    FLOAT = 'float'
    BOOL = 'boolean'
    ENUM = 'enumerate'

class Source(Enum):
    MOBILE = 'mobile'
    WEB = 'web'
    SERVER = 'server'

class ValuesValidator(ABC):

    @abstractmethod
    def validate_values(self) -> None:
        ...


@dataclass
class Property:
    name: str
    event_name: str
    type: DataType
    value_validator: Optional[ValueValidator] = None


@dataclass
class Event:
    name: str
    source:
    properties: list[Property]


@dataclass
class TrackingPlan:
    events: list[Event]


def main() -> None:
    pass

if __name__ == '__main__':
    main()
