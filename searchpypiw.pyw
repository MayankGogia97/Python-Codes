#! python3
import sys
import pyperclip
import webbrowser
import requests
from bs4 import BeautifulSoup

# Getting the link that is to be opened
if len(sys.argv) > 1:
    searchTerm = ' '.join(sys.argv[1:])

else:
    searchTerm = pyperclip.paste()
url = 'https://pypi.org/search/?q=' + searchTerm

# Scraping the webpage

res = requests.get(url)
res.raise_for_status()

# Getting all the links

soup = BeautifulSoup(res.text, 'lxml')
results = soup.find_all('a', {'class': 'package-snippet'})

# Opening the links in new tabs
for i in range(len(results)):
    link = results[i]
    resultURL = 'https://pypi.org' + link.get('href')
    webbrowser.open(resultURL)
