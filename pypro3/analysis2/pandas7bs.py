# BeautifulSoup 객체의 find(), select() 연습
from bs4 import BeautifulSoup

html_page = """
<html>
<body>
<h1>제목 태그</h1>
<p>웹 문서 읽기</p>
<p>파이썬 라이브러리 사용</p>
</body>
</html>
"""
print(html_page, type(html_page))

soup = BeautifulSoup(html_page, 'html.parser')  # BeautifulSoup 객체 생성
print(soup, type(soup))

print('------')
h1 = soup.html.body.h1
print(h1)
print('h1:', h1.string)
print('h1:', h1.text)

p1 = soup.html.body.p
print(p1)
print('p1:', p1.string)

p2 = p1.next_sibling.next_sibling
print(p2)

print('\n---find()사용 ---')
html_page2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 읽기</p>
<p id="my" class="our">파이썬 라이브러리 사용</p>
</body>
</html>
"""
soup2 = BeautifulSoup(html_page2, 'lxml')
print(soup2.p, ' ', soup2.p.string)  # 직접 최초 p tag 선택
print(soup2.find('p').string)
print(soup2.find('p', id='my').string)
print()
# print(soup2.find(['p', 'h1']))
print(soup2.find(id='my').string)
print(soup2.find(id='title').string)
print(soup2.find(class_='our').string)
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'title'}).string)

