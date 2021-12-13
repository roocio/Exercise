import pytest
from src.mongo import Order


@pytest.fixture
def order():
    return Order(
        order_number=1,
        weight=2,
        name="Maximo Cosetti",
        address1="14812 Sutter Ave",
        city="Jamaica",
        state="NY",
        postal_code="11436",
    )


def test_list_orders(clean_db, order):
    """Test to check that an order can be created deducting entirely from the product inventory"""
    order.persist()
    # todo hit /orders and check
    result = {}
    assert result == [
        dict(
            order_number=1,
            weight=2,
            name="Maximo Cosetti",
            address1="14812 Sutter Ave",
            address2="",
            city="Jamaica",
            state="NY",
            postal_code="11436",
        )
    ]


def test_create(clean_db):
    # post a json to /orders/new and check with Order.load
    ...


def test_get(clean_db, order):
    order.persist()
    # get /orders/<order.order_number> and check data is correct
    ...


def test_quote(clean_db, order):
    order.persist()
    # get /orders/<order.order_number> and check data is correct
    result = {}
    assert result["cheapest"]["rate"] == "12.3"  # update to whatever be the cheapest price
