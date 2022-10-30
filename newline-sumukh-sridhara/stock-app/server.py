from flask import Flask, render_template
import requests
from config import YOUR_API_KEY

app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com/api/v3/quote-short/{ticker}'
payload = {'apikey': YOUR_API_KEY}


def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker.upper()),
                        params=payload).json()
    return data[0]['price']


@app.route('/')
def home_page():
    return render_template('index.html')


# http://localhost:5000/stock/AAPL
@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return render_template('stock_quote.html',
                           ticker=ticker, stock_price=price)
