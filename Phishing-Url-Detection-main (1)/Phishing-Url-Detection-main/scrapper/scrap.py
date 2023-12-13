import requests
from urllib.error import URLError
from bs4 import BeautifulSoup

def crawler(website):
    url = website
    try:
        reqs = requests.get(url,timeout=2)
    except :
        print("Connection timedout")
    else:
        urls = []
        soup = BeautifulSoup(reqs.content,'html.parser')
        # print(soup)

        for link in soup.find_all('a'):
            if 'https://' in link.get('href') :
                urls.append(link.get('href'))
            # print(link.get('href'))

        return urls

# for i in 
# print(crawler('https://wikipedia.com'))