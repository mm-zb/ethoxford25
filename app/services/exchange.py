import ccxt

def get_crypto_price(symbol, exchange="binance"):
    exchange_obj = getattr(ccxt, exchange)()
    ticker = exchange_obj.fetch_ticker(symbol)
    return ticker['last']
