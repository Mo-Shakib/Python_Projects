import requests
from bs4 import BeautifulSoup
def weather(location):
    url = f'https://www.youtube.com/results?search_query=machine+learning+python'
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    temperature = s.find('div', class_='style-scope ytd-video-renderer').text
    temperature = temperature.split('°')
    return temperature[0]

print(weather(1))
