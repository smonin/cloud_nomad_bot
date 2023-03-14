from ending import end_num
import datetime
import telebot
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
bot = telebot.TeleBot(TOKEN)

today = datetime.date.today()
PAYDAY = datetime.date(2023, 4, 5)
dayz = (PAYDAY-today).days

@bot.message_handler(commands=["bonus"])
def bonus(m, res=False):
    bot.send_message(m.chat.id, end_num(dayz)) 

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)