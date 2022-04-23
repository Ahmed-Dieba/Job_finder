from os import path, getcwd
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import sqlalchemy
if path.exists(path.join(getcwd(),"data/wuzzuf.db")):
    def wuzzuf(keyword):
        '''don't forget to create database(sql or csv) file if it doesn't exist
        make the program fetch the updates only if this file isn't
        '''
        #We will pass this variable as an argument in the URL
        page_number = 0
        #This dictionary contains the headers we will send in the request
        headers_dict = {
        'authority': 'wuzzuf.net',
        'method': 'GET',
        'path': '/search/jobs/?q={}&a=hpb'.format(str(keyword)),
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'br',
        'accept-language': 'en-US,en;q=0.9' ,
        'referer': 'https://wuzzuf.net/jobs/egypt' ,
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"' ,
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        }
        #Extract the data from first 3 pages
        while page_number < 3:
            dic = {
                "address":[],
                "link":[],
                "date":[],
                "description":[],
                "location":[],
                "company":[]
                }
            url = 'https://wuzzuf.net/search/jobs/?a=hpb&q={}&start={}'.format(str(keyword),str(page_number))
            response = requests.get(url, headers=headers_dict).content
            soup = BeautifulSoup(str(response),"lxml")
            page_number+=1
            print(url)
