from typing import List, Dict

from molten import Field, schema


@schema
class OrderCreate:
    url: str = Field(description="Delivery club link")
    phone: str = Field(description="Your phone number")


@schema
class Food:
    id: int
    name: str
    description: str
    img_url: str


@schema
class Order:
    id: int
    phone: int
    food_available: List[Food]
    food_chosen: Dict[str, List[Food]]

@schema
class User:
    pass
