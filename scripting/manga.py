import requests
from bs4 import BeautifulSoup

res = requests.get("https://mangareader.to/one-piece-3")

soup = BeautifulSoup(res.text, "html.parser")

chapter_items = soup.find('li', class_='item reading-item chapter-item')
# chapter_numbers = [item['data-number'] for item in chapter_items]
print(chapter_items['data-number'])

# chapter_list = soup.find()
