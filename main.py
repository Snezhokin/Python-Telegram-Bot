from telegram.ext import Updapter , InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contens = requests.get('https://random.dog/woof.json').json()
    url = contens['https://random.dog/']
    return url

def bop (bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id = chat_id , photo = url)