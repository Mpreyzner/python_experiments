# 11 - Atomically Correct Time from Internet Clock
import requests
import bs4

url = 'https://time.is/'


def get_time(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html5lib')
    elems = soup.select('div #twd')
    yield elems[0].text.strip()


while True:
    print(next(get_time(url)))
