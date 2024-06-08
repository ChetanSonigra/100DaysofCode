import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
yc_news = response.text

yc_news = BeautifulSoup(yc_news,"html.parser")

article_texts = [x.a.getText() for x in yc_news.find_all(name="span", class_="titleline")]

article_links = [x.a.get("href") for x in yc_news.find_all(name="span",class_="titleline")]

article_scores = [int(x.getText().split()[0]) for x in yc_news.find_all(name="span", class_="score")]

max_score_index = article_scores.index(max(article_scores))
print(max_score_index)
print(article_texts[max_score_index])
print(article_links[max_score_index])
print(article_scores[max_score_index])