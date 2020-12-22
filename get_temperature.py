import requests
from bs4 import BeautifulSoup
def weather(location):
    url = f'http://www.google.com/search?&q=weather in {location}'
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    temperature = s.find('div', class_='BNeawe').text
    temperature = temperature.split('°')
    return temperature[0]

if __name__ == '__main__':
    place = input('Enter place name: ')
    print(f'Current temperature in {place} is: {weather(place)}°C')
