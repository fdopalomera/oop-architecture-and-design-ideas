from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from property import Property
from database import Database


class EventSource(Enum):
    MOBILE = 'mobile'
    WEB = 'web'
    SERVER = 'server'


@dataclass
class Event:
    name: str
    source: EventSource
    properties: list[Property]

    @classmethod
    def from_json(cls, json: dict) -> Event:
        event_name = json['name']
        event_source = json['source']
        properties = [Property(name=event_property['name'], type=event_property['type']) for event_property in json['properties']]
        return Event(name=event_name, source=event_source, properties=properties)

    def get_property_unique_values(self, property_name, database: Database) -> list[Optional[str, int]]:
        database = Database()
        pass


def main() -> None:

    event_json = {'name': 'screen_viewed',
                  'source': 'mobile',
                  'properties': [
                      {'name': 'device_os', 'type': 'enum', 'enumerators': ['ios', 'android']},
                      {'name': 'user_id', 'type': 'int'},
                      {'name': 'screen_title', 'type': 'str'}
                    ]
                  }
    event = Event.from_json(event_json)
    print(event.properties)


if __name__ == '__main__':
    main()
