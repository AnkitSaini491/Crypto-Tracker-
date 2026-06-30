from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_URL = os.getenv("COINGECKO_API")


@app.route("/")
def home():
    try:
        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 20,
            "page": 1,
            "sparkline": "false"
        }

        response = requests.get(url, params=params, timeout=10)
        coins = response.json()

    except Exception:
        coins = []

    return render_template("index.html", coins=coins)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
