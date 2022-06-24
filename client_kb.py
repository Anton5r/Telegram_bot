from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Расписание и Консультации')
b3 = KeyboardButton('/GitHub')
b4 = KeyboardButton('/Инфа')
b5 = KeyboardButton('/Контакты')
b2 = KeyboardButton('/ОбЪявление')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).insert(b4).insert(b5)