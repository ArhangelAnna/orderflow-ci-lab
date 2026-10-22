from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: int
    title: str
    price: int
    stock: int
    category: str


PRODUCTS = [
    Product(1, "Keyboard", 2700, 14, "electronics"),
    Product(2, "Mouse", 900, 26, "electronics"),
    Product(3, "Notebook", 320, 40, "office"),
    Product(4, "Pen", 110, 90, "office"),
    Product(5, "Mug", 650, 24, "home"),
    Product(6, "Lamp", 3400, 11, "home"),
]
