#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5220343201:AAEoxi70i3NVAh8SWMpo73W1nwt-VHbRpq8'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🔖 Menu")
	item2 = types.KeyboardButton("🥇 Rewards")
	item3 = types.KeyboardButton("💌 Birthday Gift Card")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Hi. Are you hungry and thirsty? I am here to help you 🤜🤛, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🔖 Menu':
			bot.send_message(message.chat.id, 'https://www.starbucks.com/menu')
		elif message.text == '🥇 Rewards':
			bot.send_message(message.chat.id, 'https://www.starbucks.com/rewards')
		elif message.text == '💌 Birthday Gift Card':
			bot.send_message(message.chat.id, 'https://www.starbucks.com/gift/873070446')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods