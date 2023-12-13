import pandas as pd
from scrap import  crawler
from csv_writer import writer
website = pd.read_csv('archive/top-1m.csv',names=['index','urls'])

# print(website.head())

for url in website['urls'][:550]:
    url = ('https://'+url)
    try:
        for i in crawler(url):
            writer([i,'benign'])
    except:
        print('Some Error')
    print(" ")