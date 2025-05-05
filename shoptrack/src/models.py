from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class CartItem:
    product_id: int
    quantity: int

@dataclass
class Order:
    order_id: int
    items: List[CartItem]
    total_amount: float
