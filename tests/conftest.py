import os

import pytest

from app.models import project_db

os.environ["MONGODB_HOST"] = os.environ.get("MONGODB_HOST", "0.0.0.0")
os.environ["MONGODB_PORT"] = "27017"
os.environ["MONGODB_USER"] = "root"
os.environ["MONGODB_PASS"] = "toor"
os.environ["MONGODB_DB"] = "shiphero"


@pytest.fixture(scope="function")
def clean_db():
    project_db.orders.delete_many({})
    project_db.product_inventory.delete_many({})
    project_db.stock_orders.delete_many({})
    project_db.allocations.delete_many({})
    yield
    project_db.orders.delete_many({})
    project_db.product_inventory.delete_many({})
    project_db.stock_orders.delete_many({})
    project_db.allocations.delete_many({})
