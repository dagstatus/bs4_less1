from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import cook



print('Вводите наименование компании')
search_name = input()

url = 'https://opencorporates.com/companies?q=MICROSOFT+CORPORATION&utf8=%E2%9C%93'

cookies = cook.cookie

def create_url (search_name_noplus):
    search_mass = str(search_name_noplus).split(' ')
    search_name_plus = ''
    for i in range(len(search_mass)):
        if i == 0:
            search_name_plus = search_mass[i]
        else:
            search_name_plus = search_name_plus + '+' + search_mass[i]
    final_url = 'https://opencorporates.com/companies?q='+ search_name_plus + '&utf8=%E2%9C%93'

    return final_url



def get_list_comp (url):
    user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
    page = requests.get(url, headers={'User-Agent':user_agent})
    soup = BeautifulSoup(page.text, "html.parser")
    print(soup)
    corp_list = soup.findAll('div', id="results")
    # return type SOUP !!!
    return corp_list

def get_list_comp_selenium(url):
    driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    driver.quit()
    # print(soup)
    corp_list = soup.findAll('div', id="results")
    # return type SOUP !!!
    return corp_list



#print(create_url(search_name))
print('-------------------FINAL--------------------')
print(get_list_comp_selenium(create_url(search_name)))
