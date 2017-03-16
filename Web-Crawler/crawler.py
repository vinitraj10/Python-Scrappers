import requests
from bs4 import BeautifulSoup

def crawl():
        url = 'http://www.makautexam.net/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('div',{'class':'block-hdnews'}):
            for i in link('a'):
                title = "http://http://www.makautexam.net/" + i.get('href')
                print(title)
crawl()
