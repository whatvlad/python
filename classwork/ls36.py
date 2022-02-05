import telebot
from telebot import types

bot = telebot.TeleBot("5284890291:AAFyS9CLOPOnNRfZUlF7BI2N9wbk3n9q-9s", parse_mode=None)


name = ""
surname = ""
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Я бот, привет!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
  if message.text.lower() == "привет":
    bot.send_message(message.from_user.id, "Привет!")
  elif message.text == "/reg":
    bot.send_message(message.from_user.id, "Как вас зовут?")
    bot.register_next_step_handler(message, nameReg)
  else:
    bot.send_message(message.from_user.id, "Я не понимаю тебя!")

def nameReg(message):
  global name
  name = message.text.lower()
  bot.send_message(message.from_user.id, "Введите вашу фамилию")
  bot.register_next_step_handler(message, surnameReg)

def surnameReg(message):
  global surname
  surname = message.text.lower()
  bot.send_message(message.from_user.id, "Введите ваш возраст")
  bot.register_next_step_handler(message, ageReg)

def ageReg(message):
  global age
  while age == 0:
    try:
      age = int(message.text)
    except Exception:
      bot.send_message(message.from_user.id, "Введите число цифрами!")
  keyword = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
  button_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
  keyword.add(button_yes, button_no)
  # keyword.add(button_no)
  ms = f"Вас зовут: {name}, ваша фамилия: {surname}, ваш возраст: {age}, верно ли?"
  bot.send_message(message.from_user.id, ms, reply_markup=keyword)

@bot.callback_query_handler(func=lambda call: True)
def queryButton(call):
  if call.data == "yes":
    bot.send_message(call.message.chat.id, "Я запомнил вас.")
  elif call.data == "no":
    bot.send_message(call.message.chat.id, "Давай попробуем ещё раз. Как вас зовут?")
    bot.register_next_step_handler(call.message, nameReg)
  else:
    bot.send_message(call.message.chat.id, "ERROR")

bot.infinity_polling()