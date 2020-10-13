#! python3
import os
import sys
import requests
import json

os.chdir(r'G:\Codes\Python')

if len(sys.argv) < 3:
    print('Not enough data...\nExiting')
    sys.exit()
elif not len(sys.argv[-1]) == 2:
    print('Country code has only two letters...\nExiting...')
    sys.exit()

api = 'https://api.openweathermap.org/data/2.5/weather?q={City},,{CountryID}&appid=d0e3d629ffd917037c633bdf91269d22&units=metric'
cityName = ' '.join(sys.argv[1:-1])
countryID = sys.argv[-1]
link = api.format(City=cityName, CountryID=countryID)

res = requests.get(link)
res.raise_for_status()

weather = json.loads(res.text)
print('This the weather for %s, %s\n\n' % (cityName, countryID))
print('The current temperature is %s°C although it feels like it is %s°C' % (weather['main']['temp'], weather['main']['feels_like']))
print('Today\'s minimum temperature will be %s°C while the maximum temperature will be %s°C' % (weather['main']['temp_min'], weather['main']['temp_max']))
print('The humidity is at %s%%\n\n' % (weather['main']['humidity']))

jsonFile = open('weather.json', 'wb')
for chunk in res.iter_content(100):
    jsonFile.write(chunk)
jsonFile.close()

print('Do you want to open the .json file?(Y/y)')
choice = input()
if choice in ['Y', 'y']:
    print('Opening...')
    os.startfile('weather.json')
