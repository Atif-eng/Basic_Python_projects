import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/news")
soup = BeautifulSoup(response.text, 'html.parser')

for headline in soup.find_all(['h1','h2','h3']):
    # print(headline.text.strip())
    news=headline.text.strip() 
        

f=open('news.txt','w')
data=f.write(news)
f.close()