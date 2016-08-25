# Creating a Telegram Bot

Let's get started! In this tutorial we'll use the Python library provided by Telegram called [python-telegram-bot](https://github.com/python-telegram-bot/).

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
	![/start command](demo/botfather_start.png "/start command")
	* /hello
	![/hello command](demo/botfather_hello.png "/hello command")
	* /caps your text
	![Caps text](demo/botfather_caps.png "Caps text")
	* Echoes messages
	![Echo text](demo/botfather_echo.png "Echo text")

## Notes

Add `@Hello_Telegram_Bot` and send him a message to test the features in this tutorial.

Get inspired by more [Examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples) with `python-telegram-bot`.

Find more infos and documentation here: [https://github.com/python-telegram-bot/](https://github.com/python-telegram-bot/)