from __future__ import annotations
from dataclasses import dataclass
from data_type import DataType, DATA_TYPES


@dataclass
class Property:
    name: str
    type: DataType

    @classmethod
    def from_dict(cls, data: dict) -> Property:
        property_name = data['name']
        type_json = data['type']
        type_name = type_json['name']

        type_object = DATA_TYPES[type_name](**type_json)

        return Property(property_name, type_object)
