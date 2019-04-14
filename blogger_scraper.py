# This one could be refined to include headings and export to a csv.

from bs4 import BeautifulSoup
import requests

source = requests.get('http://memoriasdeunamnesico.blogspot.com/search?updated-max=2002-12-06T18:11:00%2B01:00&max-results=500&start=1042&by-date=false').text

soup = BeautifulSoup(source, 'lxml')

with open("scraped_blog.txt", "w") as file:
    for entry in soup.find_all('div', class_='post-body entry-content'):
        file.write((entry.text))

    
