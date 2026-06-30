from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_URL = os.getenv("COINGECKO_API")


# Home
@app.route("/")
def home():

    try:

        response = requests.get(

            f"{BASE_URL}/coins/markets",

            params={

                "vs_currency":"usd",

                "order":"market_cap_desc",

                "per_page":20,

                "page":1,

                "sparkline":"false"

            }

        )

        coins=response.json()

    except:

        coins=[]

    return render_template("index.html",coins=coins)


# Coin Details
@app.route("/coin/<coin_id>")
def coin(coin_id):

    try:

        response=requests.get(

            f"{BASE_URL}/coins/{coin_id}"

        )

        coin=response.json()

    except:

        coin=None

    return render_template(

        "coin.html",

        coin=coin

    )


# About
@app.route("/about")
def about():

    return render_template("about.html")


# Error Pages
@app.errorhandler(404)
def page_not_found(e):

    return render_template("about.html"),404


@app.errorhandler(500)
def server_error(e):

    return render_template("about.html"),500


if __name__=="__main__":

    app.run(debug=True)
