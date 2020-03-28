import requests
from bs4 import BeautifulSoup

head1 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get("https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309", headers = head1)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
rank = 1

for song in songs:
    tag = song.select('td.info > a')

    if tag is not None:
        # a의 text를 찍어본다.
        title = song.select_one('td.info > a.title').text.lstrip()
        artist = song.select_one('td.info > a.artist').text
        print(rank,'위 /', title,'/', artist)
        rank += 1