from datetime import datetime
from random import randint

from flask import request

from src.mongo import project_db



def create_order():
    # TODO create an Order instance and persist it
    return "Order successfully created!", 200


def list_orders():
    # TODO: list every order in our db.
    return {"orders": []}


def view_order(order_id):
    # TODO: given the order return its json representation
    ...


def quote_order(order_id):
    # hit FEDEX API for the order detail and return all the result plus the cheapest one
    return {"cheapest": {"method": "foo", "price": "10.2"}, "rates": [{"method": "foo", "price": "10.2"}, {"method": "bar", "price": "15.22"}]}

