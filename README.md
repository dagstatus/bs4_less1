# Простейший парсинг новостей с новостного портала Яндекс

`https://yandex.ru/news`


Для работы необходимо установить библиотеки BeautifulSoup4 и Requests 

`pip install beautifulsoup4`


`pip install requests`


Если необходимо изменить регион новостей просто замените ссылку в переменной URL
Например:

_Новости Москвы_ `https://yandex.ru/news/region/Moscow`

_Новости экономики_ `https://yandex.ru/news/rubric/business`

_Технологические новости_ `https://yandex.ru/news/rubric/computers`

и так далее, все ссылки которые начинаются с `https://yandex.ru/news`