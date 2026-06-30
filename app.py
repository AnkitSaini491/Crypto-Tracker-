from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_URL = os.getenv("COINGECKO_API")


def get_coins():

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

        response = requests.get(url, params=params, timeout=15)

        if response.status_code == 200:

            return response.json()

        return []

    except Exception as e:

        print(e)

        return []


@app.route("/")
def home():

    coins = get_coins()

    return render_template(
        "index.html",
        coins=coins
    )


@app.route("/coin/<coin_id>")
def coin(coin_id):

    try:

        url = f"{BASE_URL}/coins/{coin_id}"

        response = requests.get(url, timeout=15)

        coin = response.json()

    except:

        coin = None

    return render_template(
        "coin.html",
        coin=coin
    )


@app.route("/about")
def about():

    return render_template("about.html")


@app.errorhandler(404)
def not_found(e):

    return render_template("about.html"),404


@app.errorhandler(500)
def error(e):

    return render_template("about.html"),500


if __name__=="__main__":

    app.run(debug=True)
