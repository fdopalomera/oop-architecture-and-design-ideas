from dataclasses import dataclass
from typing import Optional
from abc import ABC
from enum import Enum


class ValidDataType(Enum):
    STR = 'string'
    INT = 'integer'
    FLOAT = 'float'
    BOOL = 'boolean'
    ENUM = 'enumerate'


@dataclass
class DataType(ABC):
    name: str


@dataclass
class EnumType(DataType):
    enumerators: list[Optional[str, int]]


@dataclass
class StrType(DataType):
    regex_validation: Optional[str] = None


class BoolType(DataType):
    valid_values = [True, False]


class IntType(DataType):
    pass


class FloatType(DataType):
    pass


DATA_TYPES: dict[ValidDataType, DataType] = {
    ValidDataType.STR: StrType,
    ValidDataType.INT: IntType,
    ValidDataType.FLOAT: FloatType,
    ValidDataType.BOOL: BoolType,
    ValidDataType.ENUM: EnumType
}
