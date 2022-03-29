import pandas as pd
import numpy as np
import bs4
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
from urllib.request import urlretrieve 
from urllib.request import urlopen, Request
import re

def scrape_money(df):
    # 1. Input:
    search_query = df['title_urled']
    # 2. Put the title into wikipedia search and extract the link to the first result:(it's not the first link!!!)
    url = "https://en.wikipedia.org/w/index.php?search="+search_query+"&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    web_links = soup.find_all("a")
    # 3. the first result of our seach query is actually the eleventh link on the results page:
    movie_path = web_links[10].get("href")   
    # 4. now lets scrape all of the infobox-labels into a list a check how long is that list:
    response = requests.get("https://en.wikipedia.org"+movie_path)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    par_len = len(parser.find_all("th", class_="infobox-label"))
    # 5. Loop trough infobox-labels list and find the position of 'Budget':
    for num in range(8,par_len):        
        tag_name = parser.find_all("th", class_="infobox-label")[num]
        if tag_name.text == 'Budget':  
            tag_numbers = parser.find_all("td", class_="infobox-data")[num]
            return tag_numbers.text
    # 6. If we can't find the budget:
    else:
        return None