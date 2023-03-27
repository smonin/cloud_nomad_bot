import yfinance as yf

def stock_info(stock_name):
    stock = yf.Ticker(stock_name)
    list_stock = stock.info
    market_price = str(list_stock["regularMarketPrice"])
    currency = list_stock["currency"]
    symbol = list_stock["symbol"]
    short_name = list_stock["shortName"]
    return short_name + "(" + symbol + ")" +  ": " + market_price + " " + currency



