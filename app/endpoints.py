from flask import request
from app.models import Order


def create_order():
    body = request.get_json()
    # TODO create an Order instance and persist it
    return "Order successfully created!", 200


def list_orders():
    # TODO: list every order in our db.
    return {"orders": []}


def view_order(order_id):
    # TODO: given the order return its json representation
    ...


def quote_order(order_id):
    # hit FEDEX API using the lib requests
    # to return the rates results plus the cheapest one
    return {
        "cheapest": {...},
        "rates": [{
            "method": "foo",
            "price": "10.2",
            # ...
        }, ...
        ]
    }
