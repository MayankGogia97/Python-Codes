#! python3
from bs4 import BeautifulSoup
from msedge.selenium_tools import Edge, EdgeOptions
import sys
import pyperclip

# Running a search in pypi.org
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
# driver.maximize_window()
if len(sys.argv) > 1:
    searchTerm = ' '.join(sys.argv[1:])         # The search terms are in the run command
else:
    searchTerm = pyperclip.paste()              # The search terms are in the clipboard

url = 'https://pypi.org/search/?q=' + searchTerm
driver.get(url)

# Getting all the links

soup = BeautifulSoup(driver.page_source, 'lxml')
results = soup.find_all('a', {'class': 'package-snippet'})

# Extracting the link and opening in new tabs

for i in range(len(results)):
    link = results[i]
    resultURL = 'https://pypi.org' + link.get('href')
    driver.execute_script("window.open()")
    # driver.switch_to_window(driver.window_handles[i+1])      This is to be deprecated and the below is one the new one
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(resultURL)
