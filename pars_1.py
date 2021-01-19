#Пробуем спарсить новости с яндекса
# https://makhachkala.hh.ru/

from bs4 import BeautifulSoup
import requests

url='https://yandex.ru/news'

page=requests.get(url)

# Проверям статус ответа если 200 то норм
# print(page.status_code)

#Передаем в переменную типа БС4 текст страницы который мы получили
soup= BeautifulSoup(page.text, "html.parser")


#Создаем переменные для хранения новостей (черновик и чистые новости)
news=[]
news_clear_head=[]
news_clear_text=[]


#Находим все элементы с блоками новостей и загоняем их в список (черновой)
news= soup.findAll('div', class_="mg-grid__col")

#Прогоняем наш черновой список с поиском заголовка и текста новости и добавляем в финальные списки
for i in range(len(news)):
    if news[i].find('h2', class_='mg-card__title') is not None:
        news_clear_head.append(news[i].find('h2', class_='mg-card__title').text)
        news_clear_text.append(news[i].find('div', class_='mg-card__annotation').text)


#Ну и печатаем i+1 для удобства чтения стартуем с 1 вместо 0
for i in range(len(news_clear_head)):
    print(i+1, ' - ',news_clear_head[i],'\n', news_clear_text[i])

