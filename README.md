# Creating a Telegram Bot

Let's get started!

1. Fire up a command line and install the required libraries through your command line by running:

	`pip install -r requirements.txt`

2. Create or sign in to your [Telegram Account](https://web.telegram.org/)

3. Search for `@BotFather`

	![Search for @BotFather](demo/botfather_conversation.png "Search for @BotFather")

4. Initialize a conversation with the `@BotFather`

	![Initialize Conversation with BotFather](demo/botfather_init.png "Initialize Conversation with BotFather")
	
5. Create a new bot by typing `/newbot` and follow the guided process.

	Congratulations, you've created your Telegram Bot :) 

6. Generate an access token which you'll need to communicate with your bot by typing `/token`

7. Replace your Telegram access token in `telegram.py`

8. Then import `telegram.py` via `import telegram` at the top of your `main.py`

9. Your Bot supports following things:
	* /start
	* /hello
	* Echoes message

## Notes

Add `@Hello_Telegram_Bot` and send him a message to test the features in this tutorial.

Find more infos and documentation here: [https://github.com/python-telegram-bot/](https://github.com/python-telegram-bot/)


```python
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

updater = Updater('YOUR TOKEN HERE')

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
```