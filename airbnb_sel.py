import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('window-size=250,1000')

navegador = webdriver.Chrome(r'C:\Users\brunodambros\Documents\tech\scrap_airbnb\chromedriver.exe', options=options)


navegador.get('https://www.airbnb.com.br/')

sleep(3)

input_place = navegador.find_element('input')

input_place.send_keys('Itália')
input_place.submit()

