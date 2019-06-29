from molten import Route

from . import views

routes = [
    Route("/api/order", views.create, "POST"),
    Route("/api/order/{order_id}", views.get, "GET"),
]
