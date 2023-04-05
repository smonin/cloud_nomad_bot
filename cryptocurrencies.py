from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyCodes

def my_btc_converter(currency):

    cc = CurrencyCodes()
    b = BtcConverter()
    return str(int(b.get_latest_price(currency))) + cc.get_symbol(currency)

