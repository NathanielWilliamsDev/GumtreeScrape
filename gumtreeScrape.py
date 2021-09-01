# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:16:40 2021

@author: Natha
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


jobList = []


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    url = f'https://www.gumtree.com.au/s-cars-vans-utes/silvia/page-{page}/k0c18320'
    r = requests.get(url, headers) # 200 is OK, 404 is page not found
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('a', class_ = 'user-ad-row-new-design user-ad-row-new-design--featured-or-premium user-ad-row-new-design--cars-category link link--base-color-inherit link--hover-color-none link--no-underline')
    print(len(divs))
    for item in divs:
        # skip certain items
#        if item.find(class_ = 'label'):
#            continue # need to fix, if finds a job that has a 'new' span before the title span, skips job completely
        title = item.find('span', class_ ='user-ad-row-new-design__title-span').text.strip()
        print(title)
        price = item.find('span', class_ = "user-ad-price-new-design__price").text.strip()
        #print(price)
        description = item.find('p', class_ = "user-ad-row-new-design__description-text").text.strip() #.replace('\n', '')
        #print(description)
#       finding info that isn't present for all containers 
#        try:
#            salary = item.find('span', class_ = "salary-snippet").text.strip()
#        except:
#            salary = ""
        
#        job = {
#                'title': title,
#                'price': price,
#                'description': description
#        }
#        jobList.append(job)
#        print("Seeking a: "+title+" to join: "+company+" paying: "+salary+". Job description: "+description) 
    return

test = extract(1)
transform(test)



