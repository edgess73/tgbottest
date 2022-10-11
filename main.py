import telebot #импорт библиотеки
from telebot import types
import random

bot = telebot.TeleBot('TOKEN') #Сюда вводить токен бота
@bot.message_handler(commands=['start']) #Реакция на /start
def start(message):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True) #Добавление кнопок в разметку
    btn1 = types.KeyboardButton("Понятно")
    mrk.add(btn1)
    bot.send_message(message.chat.id, text="Привет! Это просто тестовый бот справочник. Тут ты можешь получить разную информацию или случайный факт.".format(message.from_user), reply_markup=mrk) #Приветственное сообщение
@bot.message_handler(content_types=['text']) #Бот реагирует на текстовые команды
def func(message):
    if(message.text == "Понятно"):
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎲 Случайный факт")
        btn2 = types.KeyboardButton("🔗 Ссылка на феди")
        btn3 = types.KeyboardButton("ℹ️ Инфо о боте")
        mrk.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вот и славно что всё понятно, а теперь нажми на любую из кнопок и я пришлю тебе сообщение".format(message.from_user), reply_markup=mrk)
    elif(message.text == "🔗 Ссылка на феди"):
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎲 Случайный факт")
        btn2 = types.KeyboardButton("🔗 Ссылка на феди")
        btn3 = types.KeyboardButton("ℹ️ Инфо о боте")
        mrk.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Ссылка на Fediverse создателя: @edgesdragon@shitpost.poridge.club".format(message.from_user), reply_markup=mrk)
    elif(message.text == "ℹ️ Инфо о боте"):
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎲 Случайный факт")
        btn2 = types.KeyboardButton("🔗 Ссылка на феди")
        btn3 = types.KeyboardButton("ℹ️ Инфо о боте")
        mrk.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Данный бот был создан как тест библиотеки PyTelegramBotAPI, что собственно и делает. Возможно я переведу бота жс или дополню, а пока он будет висеть в фоне до конца дня. #KC".format(message.from_user), reply_markup=mrk)
    elif(message.text == "🎲 Случайный факт"):
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎲 Случайный факт")
        btn2 = types.KeyboardButton("🔗 Ссылка на феди")
        btn3 = types.KeyboardButton("ℹ️ Инфо о боте")
        mrk.add(btn1, btn2, btn3)
        facts = ["Ты милый!", "Сегодня прекрасный день", "Евгепес ленивая жопка", "Ник hentaihunter появился из-за того, что евгепес не мог придумать что-то другое к буквам HH", "У naebnet классное интро", "евгепес не знает пухтон", "Bruh moment", "Если бы с рождения давали выбор языка, я бы выбрал язык фактов"]
        fact = random.choice(facts)
        bot.send_message(message.chat.id, text = fact.format(message.from_user), reply_markup=mrk)

bot.polling()
