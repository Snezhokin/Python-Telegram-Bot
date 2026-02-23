from telegram.ext import Updapter , CommandHandler
import requests
import re

def get_url():
    contens = requests.get('https://random.dog/woof.json').json()
    url = contens['https://random.dog/']
    return url

