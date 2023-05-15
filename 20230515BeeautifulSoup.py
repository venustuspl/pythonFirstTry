import requests as req
from bs4 import BeautifulSoup
strona=req.get('http://jsystems.pl/static/data/pnl/dane.html')
strona.encoding='utf-8'
zupa=BeautifulSoup(strona.text,'html.parser')