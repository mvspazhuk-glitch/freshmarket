from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", year=datetime.now().year)

@app.route("/products")
def products():
    return render_template("products.html", year=datetime.now().year)

@app.route("/cart")
def cart():
    return render_template("cart.html", year=datetime.now().year)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html", year=datetime.now().year)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)