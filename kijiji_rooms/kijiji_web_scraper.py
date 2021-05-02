import requests
import re

from bs4 import BeautifulSoup


pageNum = 1

minPrice = 450

maxPrice = 700


url='https://www.kijiji.ca/b-for-rent/mississauga-peel-region/room/page-' + str(pageNum) + 'k0c30349001l1700276?rb=true&ll=43.733835%2C-79.823181&address=11965+Hurontario+Street%2C+Brampton%2C+ON&ad=offering&radius=11.0&dc=true'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')


infoList = html.findAll('div', class_='search-item')

class Room:
    price = ''
    title = ''

    link = ''
    distance = ''
    imageUrl = ''

rooms = []

for info in infoList:

    room = Room()

    room.price = info.find('div', class_='price').string.strip()

    if re.search('[a-zA-Z]', room.price) == None:

        priceFloat = float(room.price.strip('$').replace(',', ''))

        if not(minPrice <= priceFloat <= maxPrice):
            continue

    room.title = info.find('a', class_='title').string.strip()

    room.link = info.find('a', class_='title').get('href')

    room.distance = info.find('div', class_='distance').string.strip()
    room.imageUrl = info.find('img').get('data-src', None)
    if room.imageUrl == None:
        room.imageUrl = info.find('img')['src']
        
    rooms.append(room)