import telebot

bot = telebot.TeleBot("5284890291:AAFyS9CLOPOnNRfZUlF7BI2N9wbk3n9q-9s", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Я бот, привет!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
  if message.text == "привет":
    bot.reply_to(message, "Привет!")
  elif message.text == "как ты":
    bot.reply_to(message, "Норм!")
  elif message.text == "как дела":
    bot.reply_to(message, "Отлично!")
  elif message.text == "сколько тебе лет?":
    bot.reply_to(message, "16!")
  elif message.text == "Что делаешь?":
    bot.reply_to(message, "Ничего, я же бот!")
  else:
    bot.reply_to(message, "Я тебя не понимаю(")

bot.infinity_polling()