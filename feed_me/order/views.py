import shelve
import uuid

from molten import http
from molten.errors import HTTPError

from feed_me.order.schema import OrderCreate, Order, Food, User
from .parser import parse


class Orders:
    path = "./storage"

    def save(self, id_, obj):
        with shelve.open(self.path) as fh:
            fh[id_] = obj

    def get(self, id_):
        with shelve.open(self.path) as fh:
            return fh.get(id_)


ORDERS = Orders()


def create(order: OrderCreate) -> Order:
    order_nr = uuid.uuid4().hex
    food = parse(order.url)
    available_food = [
        Food(id=f.product_id, name=f.name, description=f.description, img_url=f.img_url)
        for f in food
    ]

    order_ready = Order(
        id=order_nr,
        phone=order.phone,
        food_available=available_food,
        food_chosen=[],
    )
    ORDERS.save(order_nr, order_ready)
    return order_ready


def get(order_id: str) -> Order:
    order = ORDERS.get(order_id)
    if not order:
        raise HTTPError(http.HTTP_404, "order not found")

    return order

def add_user(order_id: str, user: User):
    return
