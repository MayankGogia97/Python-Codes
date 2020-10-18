import time
from bs4 import BeautifulSoup
import requests
import os
import threading
import sys

startTime = time.time()


def downloadXKCD(startComic, endComic):

    """Each thread downloads the chunk of comics within the two parameters

    Args:
        startComic (int): [where the chunk of comics starts]
        endComic (int): [where the chunk of comics end]
    """

    for comicNum in range(startComic, endComic+1):

        print(f'Downloading page https://xkcd.com/{comicNum}/...')
        if comicNum in [404, 1525, 2067]:
            print('Skipping this page...')
            continue

        res = requests.get(f'https://xkcd.com/{comicNum}/', headers=header)
        soup = BeautifulSoup(res.text, 'lxml')
        comic = soup.find('div', {'id': 'comic'})

        if comic.img is None:
            print('This page doesn\'t contain an image. Skipping...')
            continue

        print(f"Downloading image from https:{comic.img.get('src')}...")
        imglink = f"https:{comic.img.get('src')}"
        imgresult = requests.get(imglink, headers=header)

        print(f'Saving image XKCD {comicNum}.png')
        imgFile = open(f'XKCD {comicNum}.png', 'wb')
        for imgchunk in imgresult.iter_content(100000):
            imgFile.write(imgchunk)
        imgFile.close()


header = {'user-agent': 'Chrome'}
res = requests.get('https://xkcd.com', headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
result = soup.find('div', {'id': 'middleContainer'})
lines = (result.getText().strip()).split('\n')
linksplit = lines[-2].split('/')
latest = int(linksplit[-2])
os.chdir('G:\\Codes\\Python\\XKCD(Threading)')
downloadThreads = []

if os.path.isfile('lastComic.txt'):
    lastComicHistoryFile = open('lastComic.txt')
    lastDownloaded = int(lastComicHistoryFile.readline())
    lastComicHistoryFile.close()

else:
    lastDownloaded = 0

if lastDownloaded == latest:
    print('All images are already backed up...')
    sys.exit()

numThreads = 100
groupSize = int((latest-lastDownloaded)/numThreads)

if groupSize == 0:
    groupSize = 1

for i in range(lastDownloaded+1, latest+1, groupSize):
    start = i
    end = i + groupSize - 1
    downloadThread = threading.Thread(target=downloadXKCD, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

lastComicHistoryFile = open('lastComic.txt', 'w')
lastComicHistoryFile.write(str(latest))
lastComicHistoryFile.close()


timeElapsed = time.time() - startTime
hours = int(timeElapsed / 3600)
minutes = int((timeElapsed % 3600) / 60)
seconds = timeElapsed % 60
print(f'Backup finished.\nBackup took {hours} hours {minutes} minutes and {seconds} seconds.')
performanceHistoryFile = open('elapsedTime.txt', 'a')
performanceHistoryFile.write(f'{latest-lastDownloaded} comics took {hours} hours {minutes} minutes and {seconds} seconds({numThreads}).')
performanceHistoryFile.write('\n')
performanceHistoryFile.close()
