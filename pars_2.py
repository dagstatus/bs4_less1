# Пробуем спарсить новости с яндекса
# https://yandex.ru/news

from bs4 import BeautifulSoup
import requests
import proxy
import time

proxies_all=proxy.get_free_proxies()
url = 'https://yandex.ru/news/region/makhachkala'

page = requests.get(url)

# Проверям статус ответа если 200 то норм
print(page.status_code)

# Передаем в переменную типа БС4 текст страницы который мы получили
soup = BeautifulSoup(page.text, "html.parser")

# Создаем переменные для хранения новостей (черновик и чистые новости)
news = []
news_clear_head = []
news_clear_text = []
news_url = []
news_url_yapages = []
news_source_urls = []
news_url_clear = []

# Находим все элементы с блоками новостей и загоняем их в список (черновой)
news = soup.findAll('div', class_="mg-grid__col")


# Прогоняем наш черновой список с поиском заголовка и текста новости и добавляем в финальные списки
for i in range(len(news)):
    if news[i].find('h2', class_='mg-card__title') is not None:
        news_clear_head.append(news[i].find('h2', class_='mg-card__title').text)
        news_clear_text.append(news[i].find('div', class_='mg-card__annotation').text)
        news_url.append(news[i].find('a', class_='mg-card__link', href=True)['href'])
        #
        # Создаем еще одну переменную page_tmp для перехода на страницу новости
        page_tmp = requests.get(news[i].find('a', class_='mg-card__link', href=True)['href'])
        for x in range(5):
            print(x+1)
            time.sleep(1)
        # Передаем в новую переменную типа БС4 текст страницы который мы получили
        soup_tmp = BeautifulSoup(page_tmp.text, "html.parser")
        news_url_yapages = soup_tmp.findAll('div', class_='news-story__source')
        news_source_urls.clear()
        for x in range(len(news_url_yapages)):
            if news_url_yapages[x].find('div', class_='mg-snippet__content') is not None:
                news_source_urls.append(news_url_yapages[x].find('a', class_='mg-snippet__url', href=True)['href'])
                print(news_source_urls)
        news_url_clear.append(news_source_urls)

# Ну и печатаем i+1 для удобства чтения стартуем с 1 вместо 0


for i in range(len(news_clear_head)):
    print(i + 1, ' - ', news_clear_head[i], '\n', news_clear_text[i], '\n', news_url_clear[i])

