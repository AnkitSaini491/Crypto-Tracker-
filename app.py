from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_URL = os.getenv("COINGECKO_API", "https://api.coingecko.com/api/v3")


def get_market_data():
    url = f"{BASE_URL}/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Market Error:", e)
        return []


def get_coin_data(coin_id):
    url = f"{BASE_URL}/coins/{coin_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Coin Error:", e)
        return None


@app.route("/")
def home():

    coins = get_market_data()

    return render_template(
        "index.html",
        coins=coins
    )


@app.route("/coin/<coin_id>")
def coin(coin_id):

    coin = get_coin_data(coin_id)

    if coin is None:
        return render_template("404.html"),404

    return render_template(
        "coin.html",
        coin=coin
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"),500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT",5000)),
        debug=True
    )
