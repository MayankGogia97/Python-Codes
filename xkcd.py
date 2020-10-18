<<<<<<< HEAD
#! python3
import os
import requests
from bs4 import BeautifulSoup
import time
import re

start = time.time()
url = 'https://xkcd.com'
headers = {'user-agent': 'Chrome'}
os.chdir(r'G:\Codes\Python\XKCD')

while not url.endswith('#'):
    print('Downloading Page %s' % (url))
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    comic = soup.find('div', {'id': 'comic'})
    prev = soup.find('a', {'rel': 'prev'})
    num = re.compile(r'\d+')
    nameSlice = num.search(url)
    if nameSlice is None:
        name = soup.find('div', {'id': 'middleContainer'})
        texts = (name.getText().strip()).split('\n')
        splittexts = texts[-2].split('/')
        comicname = splittexts[-2] + '.png'
        latest = splittexts[-2]
    else:
        if nameSlice.group() in ['1525', '2067']:      # Non image sites that break the code
            url = 'https://xkcd.com' + prev.get('href')
            print('Skipping this page\n')
            continue
        comicname = nameSlice.group() + '.png'
    url = 'https://xkcd.com' + prev.get('href')
    if comic.img is None:
        print('This page doesn\'t contain an image\n')
        continue
    if os.path.isfile(comicname):
        print('File already exists.\nExiting')
        break
    imglink = 'https:' + comic.img.get('src')
    print('Downloading Image %s' % (imglink))
    imgres = requests.get(imglink, headers=headers)
    print('Saving Image %s\n' % (comicname))
    imageFile = open(comicname, 'wb')
    for chunk in imgres.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
print('Done')
timeElapsed = time.time() - start
hours = int(timeElapsed / 3600)
minutes = int((timeElapsed % 3600) / 60)
seconds = timeElapsed % 60
print(f'Backup finished.\nBackup took {hours} hours {minutes} minutes and {seconds} seconds.')
perfFile = open('xkcdElapsedTime.txt', 'a')
perfFile.write(f'{latest} comics took {hours} hours {minutes} minutes and {seconds} seconds.')
perfFile.close()
=======
#! python3
import os
import requests
from bs4 import BeautifulSoup
import time
import re

start = time.time()
url = 'https://xkcd.com'
headers = {'user-agent': 'Chrome'}
while not url.endswith('#'):
    print('Downloading Page %s' % (url))
    res = requests.get(url, headers=headers)
    os.chdir(r'G:\Codes\Python\XKCD')
    soup = BeautifulSoup(res.text, 'lxml')
    comic = soup.find('div', {'id': 'comic'})
    prev = soup.find('a', {'rel': 'prev'})
    num = re.compile(r'\d+')
    nameSlice = num.search(url)
    if nameSlice is None:
        name = soup.find('div', {'id': 'middleContainer'})
        texts = (name.getText().strip()).split('\n')
        splittexts = texts[-2].split('/')
        comicname = splittexts[-2] + '.png'
        latest = splittexts[-2]
    else:
        if nameSlice.group() in ['1525', '2067']:      # Non image sites that break the code
            url = 'https://xkcd.com' + prev.get('href')
            print('Skipping this page\n')
            continue
        comicname = nameSlice.group() + '.png'
    url = 'https://xkcd.com' + prev.get('href')
    if comic.img is None:
        print('This page doesn\'t contain an image\n')
        continue
    if os.path.isfile(comicname):
        print('File already exists.\nExiting')
        break
    imglink = 'https:' + comic.img.get('src')
    print('Downloading Image %s' % (imglink))
    imgres = requests.get(imglink, headers=headers)
    print('Saving Image %s\n' % (comicname))
    imageFile = open(comicname, 'wb')
    for chunk in imgres.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
print('Done')
timeElapsed = time.time() - start
hours = int(timeElapsed / 3600)
minutes = int((timeElapsed % 3600) / 60)
seconds = timeElapsed % 60
print(f'Backup finished.\nBackup took {hours} hours {minutes} minutes and {seconds} seconds.')
perfFile = open('xkcdElapsedTime.txt', 'a')
perfFile.write(f'{latest} comics took {hours} hours {minutes} minutes and {seconds} seconds.')
perfFile.close()
>>>>>>> 52fea2f505e84c4b060a65b0f29eb3761e616569
