import os

os.system(r'pip install --upgrade pip')
os.system(r'pip install aiogram')
os.system(r'pip install asyncio')
os.system(r'pip install db-sqlite3')
os.system(r'pip install terminal_banner')
os.system(r'clear')

print("Хотите запустить Бота?")
a = input("yes/no: ")

if a == 'yes':
    os.system(r'python3 start.py')
elif a == 'no':
    os,system(r'clear')
    print('Команда для запуска: python3 start.py')
