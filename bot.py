from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
from config import TOKEN
import terminal_banner
import os
import sqlite3
from time import *
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from client_kb import *
import logging
from pyfiglet import Figlet

# Начала
os.system(r'clear')
# banner_text = "Бот-aiogram запущен в Альфа-тест\n Версия v1.0\n Путь до файла--/home/anton/Bot-aiogrm/bot.py"
# my_banner = terminal_banner.Banner(banner_text)
# print(my_banner)

banner = Figlet(font='asc_____')
print(banner.renderText('Start bot'))

logging.basicConfig(level=logging.INFO)

cur_date = datetime.now().strftime("%Y-%m-%d")
cur_time = datetime.now().time()

ADMIN =  # ваш user-id. Узнать можно тут @getmyid_bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INTEGER,
   block INTEGER);
""")
conn.commit()

# #Создание клавы
urlkb = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text="Расписание", url="https://docs.google.com/spreadsheets/d/1IHbo9mHPpdk1_-23g6iqG97kLzhHPpqtlbAlWKRFIuE/edit#gid=2137778921")
btn2 = InlineKeyboardButton(text="Консультации", url='https://docs.google.com/spreadsheets/d/11b4EHHMQ4suZ1KafsSeHHa4Bf7kYUQNBB_2UIlt0Xtw/edit?usp=sharing')
urlkb.add(btn1).add(btn2)

gitkb = InlineKeyboardMarkup(row_width=1)
btn3 = InlineKeyboardButton(text="GitHub", url="https://github.com")
gitkb.add(btn3)

abouts = InlineKeyboardMarkup(row_width=1)
about_1 = InlineKeyboardButton(text='Официальный сайт:', url = 'www.urtt.ru')
abouts.add(about_1)

newsbut = InlineKeyboardMarkup(row_width=1)
news_1 = InlineKeyboardButton(text='Web-приложение для расписание', url = 'https://timee.space/')
newsbut.add(news_1)

# Сам код бота
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEEYepiTIyHQdOjw-H7pYs8qw_HE-MTNwAClwUAAsEYngsruBWrgVvc2yME')
    await bot.send_message(message.from_user.id, text="Привет", reply_markup=kb_client)
    print(str(message.from_user.username) + " - " + str(message.from_user.id))

    id = str(message.from_user.username) + " - " + str(message.from_user.id)

    with open('user_id_list.txt', 'a+') as file:
        file.write(f'user_id: {id} - {cur_time} - {cur_date}\n')
        print('Пользователь добавлен\n')

@dp.message_handler(commands=['Расписание'])
async def rasp(message: types.Message):
    os.system(r'python /home/mrx/Bot-aiogrm/parser.py')
    await bot.send_message(message.from_user.id, text='Держи', reply_markup=urlkb)
    # await bot.send_message(message.from_user.id, text='.', reply_markup=kb_client)
    await bot.send_message(message.from_user.id, 'Если ссылка сверху не работает')
    await message.answer_document(open(file=f'link-{cur_date}.txt', mode='rb'))
    await bot.send_message(message.from_user.id, 'Обновление расписание делается раз в неделю(В Воскресение)')
    print(str(message.from_user.username) + " - " + str(message.from_user.id))

    id = str(message.from_user.username) + " - " + str(message.from_user.id)

    with open('user_id_list.txt', 'a+') as file:
        file.write(f'Кто запрашивал расписание: {id} - {cur_time} - {cur_date}\n')
        print('Пользователь добавлен\n')

@dp.message_handler(commands=['ОбЪявление'])
async def news(message: types.Message):
    await bot.send_message(message.from_user.id, 'Появился сайт/web-приложение для просмотра расписание. Более детально можно почитать в официальной группе вк: https://vk.com/wall-58074160_14574')
    await bot.send_message(message.from_user.id, 'Создатель этого web-приложения: https://vk.com/vladislavbabinov')
    await bot.send_message(message.from_user.id, 'Сама ссылка на приложение снизу', reply_markup=newsbut)

@dp.message_handler(commands=['GitHub'])
async def github(message: types.Message):
    await bot.send_message(message.from_user.id, text='Тут будет находиться проект', reply_markup=gitkb)

@dp.message_handler(commands=['Инфа'])
async def about(message: types.Message):
    await bot.send_message(message.from_user.id, text='Тут информация о коледже', reply_markup=abouts)

@dp.message_handler(commands=['Контакты'])
async def contact(message: types.Message):
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEEYe5iTI4TkPZEltGp8hA8sgWEpO9UPAACqAYAAsEYnguco4sqQ7MM4CME')
    await bot.send_message(message.from_user.id, 'Если у вас есть предложение или идеи для улучшения бота, то пишите: @atomizer78th', reply_markup=kb_client)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEEYBFiS_6kOODCYT3uskr0H5Z9F5Ko2wACwhMAAkCBIUosvecs3WT7UCME')
    await bot.send_message(message.from_user.id, 'Если не появляются новые функции, то пропишите /start')

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_sticker(msg.from_user.id, 'CAACAgIAAxkBAAEEYA9iS_3Miu4BNl0-xuIdCw3oqnrXhwACIAYAAlojPQvBymEdcoc7yiME')
    await bot.send_message(msg.from_user.id, 'Введите /help или /start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
