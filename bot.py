from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

# Methods handling commands

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')

def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


# Helpers

echo_handler = MessageHandler([Filters.text], echo)

updater = Updater('269099404:AAFVA72KeKpzg16Nma2TI6HB4tfCJ6S8jA4')

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
