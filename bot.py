# -*- coding: utf-8 -*-

from telebot import types
import config
import telebot
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['pidor'])
def handle_start_help(message):
    p = random.random()
    pidor = round(p)
    ap = {}
    if pidor == 1:
        bot.send_message(message.chat.id, "Ты пидор!")
        ap["pidor1"] = True
    else:
        ap["pidor1"] = False
        bot.send_message(message.chat.id, "Ты не пидор!")

    if ap["pidor1"] is True:
        val = random.random()
        valka = round(val)
        if valka == 1:
            bot.send_message(message.chat.id, "Ты пасив!")

        else:
            bot.send_message(message.chat.id, "Ты актив!")

    pass

if __name__ == '__main__':
     bot.polling(none_stop=True)