from flask import Flask

from src.enpoints import list_orders, create_order, view_order, quote_order

app = Flask(__name__)

app.add_url_rule("/orders", "list_orders", view_func=list_orders, methods=["GET"])
app.add_url_rule("/orders/new", "create_order", view_func=create_order, methods=["POST"])
app.add_url_rule("/order/<int:post_id>", "view_order", view_func=view_order, methods=["GET"])
app.add_url_rule("/order/<int:post_id>/quote", "quote_order", view_func=quote_order, methods=["GET"])


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
