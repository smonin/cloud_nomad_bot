from cryptocurrencies import my_btc_converter
from stocks import stock_info
from ending import end_num
import datetime
import telebot
from telebot import types
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
bot = telebot.TeleBot(TOKEN)

today = datetime.date.today()
PAYDAY = datetime.date(2023, 4, 5)
dayz = (PAYDAY-today).days

@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(  
        message.chat.id,  
        'Greetings!\n' +  
        'Bonus information - press /bonus\n' + 
        'Stocks information - press /stocks\n' +  
        'Bitcoin price information - press /crypto\n' +
        'Help page - press /help.'  
    )

@bot.message_handler(commands=['help'])     
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(  
        telebot.types.InlineKeyboardButton(  
            'Message the developer', url='telegram.me/stan_devops'  
        )  
    )  
    bot.send_message(  
        message.chat.id,
        'The Cloud nomad bot development is in progress, \n' +
        'but you can try some commands... \n' +
        'Bonus information - press /bonus\n' +
        'Stocks information - press /stocks\n' + 
        'Bitcoin price information - press /crypto\n' +  
        'Stay tuned and new features will appear soon!',  
        reply_markup=keyboard  
    )

@bot.message_handler(commands=["bonus"])
def bonus(m, res=False):
    bot.send_message(m.chat.id, 'Дождались! Твой проект тю-тю, ищи работу!')


@bot.message_handler(commands=["crypto"])
def crypto_command(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("USD")
    but2 = types.KeyboardButton("EUR")
    but3 = types.KeyboardButton("GBP")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)

    bot.send_message(  
        message.chat.id,
        'Press "USD" button to get Bitcoin price in $ \n' +
        'Press "EUR" button to get Bitcoin price in € \n' +
        'Press "GBP" button to get Bitcoin price in £ \n',
         
        reply_markup=markup
    )

@bot.message_handler(commands=["stocks"])
def stocks_command(message):
    
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("MSFT")
    but2 = types.KeyboardButton("AAPL")
    but3 = types.KeyboardButton("INTC")
    but4 = types.KeyboardButton("NVDA")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)

    bot.send_message(  
        message.chat.id,
        'Press "MSFT" button to get info about Microsoft stocks, \n' +
        'Press "AAPL" button to get info about Apple stocks, \n' +
        'Press "INTC" button to get info about Intel stocks, \n' + 
        'Press "NVDA" button to get info about Nvidia stocks.', #\n' +   
        #'or just type a known NASDAQ symbol of a needed company.',  
        reply_markup=markup
    )

@bot.message_handler(content_types=["text"])
def handle_text_1(message):
    if message.text.strip() == "MSFT":
        reply = stock_info("MSFT")
    elif message.text.strip() == "AAPL":
        reply = stock_info("AAPL")
    elif message.text.strip() == "INTC":
        reply = stock_info("INTC")
    elif message.text.strip() == "NVDA":
        reply = stock_info("NVDA")
    elif message.text.strip() == "USD":
        reply = my_btc_converter("USD")
    elif message.text.strip() == "EUR":
        reply = my_btc_converter("EUR")
    elif message.text.strip() == "GBP":
        reply = my_btc_converter("GBP")
    #elif message.text.strip() == message.text:
    #    reply = stock_info(message.text)
    

    bot.send_message(message.chat.id, reply)
        

    

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)