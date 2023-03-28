from currency import stock_info
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
        'To get the bonus information press /bonus\n' + 
        'To get stocks information press /stocks\n' +  
        'To get help press /help.'  
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
        '1) To receive the bonus information press /bonus\n' +
        '2) To receive stocks information press /stocks\n' +   
        'Stay tuned and new features will appear soon!',  
        reply_markup=keyboard  
    )

@bot.message_handler(commands=["bonus"])
def bonus(m, res=False):
    bot.send_message(m.chat.id, end_num(dayz)) 

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
        'Press "NVDA" button to get info about Nvidia stocks, \n' +   
        'or just type a known NASDAQ symbol of a needed company.',  
        reply_markup=markup
    )

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "MSFT":
        reply = stock_info("MSFT")
    elif message.text.strip() == "AAPL":
        reply = stock_info("AAPL")
    elif message.text.strip() == "INTC":
        reply = stock_info("INTC")
    elif message.text.strip() == "NVDA":
        reply = stock_info("NVDA")

    bot.send_message(message.chat.id, reply)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)