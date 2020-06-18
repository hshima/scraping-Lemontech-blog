import json

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.lemontech.com.br/lemonnews/")
# res = requests.get("https://pt.wikipedia.org/wiki/Portal:Geografia")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_='post')

all_posts = []
for post in posts:
    info = post.find(class_='post-content')
    title = info.h4.text
    preview = info.p.text
    date = info.find(class_='updated').text
    author = info.find(rel='author').text
    all_posts.append(
        {
            'title': title,
            'preview': preview,
            'date': date,
            'author': author
        }
    )
# print(all_posts)
with open('lemontechBlog.json','w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)