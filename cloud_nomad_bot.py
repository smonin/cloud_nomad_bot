from ending import end_num
import datetime
import telebot
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
        'To get the bonus information press /bonus.\n' +  
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
        '1) To receive the bonus information press /bonus.\n' +    
        'Stay tuned and new features will appear soon!',  
        reply_markup=keyboard  
    )

@bot.message_handler(commands=["bonus"])
def bonus(m, res=False):
    bot.send_message(m.chat.id, end_num(dayz)) 

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)