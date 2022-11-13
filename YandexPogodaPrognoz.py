import requests
import bs4

response = requests.get("https://yandex.ru/pogoda/")
print(response.status_code)

tree = bs4.BeautifulSoup(response.text, 'html.parser')

for item in tree.select(".card"):
    obj = item.select_one('.title-icon__text')
    if (obj is not None):
        print(obj.text)

count = 0
for item in tree.select(".forecast-briefly__day"):
    res = item.find('a').attrs['aria-label']
    if (count > 2) & (count < 9):
        print(res)
    count+=1

