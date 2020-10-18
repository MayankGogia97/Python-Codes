#!python3
from bs4 import BeautifulSoup
import webbrowser
import requests
import sys
import pyperclip
# from msedge.selenium_tools import Edge, EdgeOptions

if len(sys.argv) > 1:
    searchTerm = ' '.join(sys.argv[1:])

else:
    searchTerm = pyperclip.paste()
searchURL = 'https://amazon.in/s?k=' + searchTerm
res = requests.get(searchURL, headers={'user-agent': 'Chrome'})
res.raise_for_status()
# options = EdgeOptions()
# options.use_chromium = True
# options.headless = True
# driver = Edge(options=options)
# driver.get(searchURL)
# soup = BeautifulSoup(driver.page_source, 'lxml')
soup = BeautifulSoup(res.text, 'lxml')
results = soup.find_all('div', {'data-component-type': 's-search-result'})
for i in range(len(results)):
    item = results[i]
    productURl = 'https://amazon.in' + item.h2.a.get('href')
    webbrowser.open(productURl)
# driver.quit()
