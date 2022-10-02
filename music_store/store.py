from dataclasses import dataclass
from enum import Enum


class Genre(Enum):
    ROCK = "Rock"
    METAL = "Metal"
    POP = "Pop"


class OpticalDiscType(Enum):
    CD = "Compact Disc"
    SACD = "Super Audio Compact Disc"
    HDCD = 'High Definition Compact Disc'


class ProductDefaultMargin(Enum):
    OPTICAL_DISC = .4
    VINYL = .5


@dataclass
class Product:
    cost_clp: int
    barcode: int
    stock: int

    def update_stock(self, quantity: int) -> None:
        """Update the stock of the product by adding or substracting a certain amount of products"""
        self.stock = self.stock + quantity  # TODO: Only allow positive integers or 0 as valid stock values

@dataclass
class OpticalDisc(Product):
    genre: Genre = Genre.ROCK
    type: OpticalDiscType = OpticalDiscType.CD


@dataclass
class Vinyl(Product):
    genre: Genre = Genre.ROCK


@dataclass
class Inventory:
    products_list = list[Product]

    def get_catalog(self) -> list[str]:
        """Retrieve a list of the products in stock"""
        pass
