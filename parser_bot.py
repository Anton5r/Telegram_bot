from bs4 import BeautifulSoup
import requests
from datetime import datetime

    # Смотреть в (Иследование страници в 'сети')
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

    # Основной код проги
def get_data(url):
    cur_date = datetime.now().strftime("%Y-%m-%d")

       # Запрос к сайту и копируем его страницу
    response = requests.get(url=url, headers=headers)#
    print(response.status_code)
    
    with open(file='index.html', encoding='utf-8', mode='w') as file:
        file.write(response.text)
    
    with open(file='index.html') as file:
        src = file.read()
    
    # Вызываем страницу(14-18 строка) и ищем по ней div( ul( li( a( href(ссылка)))))
    soup = BeautifulSoup(src, 'lxml')
    div_li_a = soup.find('div', {'class': 'gem-list gem-list-type-star gem-list-color-5'}).find('ul').find('li').find('a').get('href')
    print('Успех. !!!!!')
    
    # Записываем в файл. Каждый раз  новой строки 
    with open(f"link-{cur_date}.txt", "w") as f:
        f.write("Url in link: " + str(div_li_a))
        f.write("\n")
        f.close()
    
    # Ссылка на ссайт для парсера
def main():
    get_data(url='https://urtt.ru/students/dnevnoe/raspisaniya/')
        
    
    # По стандарту
if __name__ == '__main__':
    main()