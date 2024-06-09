import requests
from bs4 import BeautifulSoup

# We are going to scrape: https://github.com/topics/
# For each topic, we will get a list of topic title, topic id and topic page url
# For each topic, we will get top 25 repo from in topic from topic page.
# details: repo_name, username, stars, repourl
github_url = "https://github.com"
topics_url = "https://github.com/topics"

response = requests.get(topics_url)
print(response.status_code)

page_contents = response.text
topics_soup = BeautifulSoup(page_contents,"html.parser")

topic_names = [x.getText() for x in topics_soup.select(selector="a p[class='f3 lh-condensed mb-0 mt-1 Link--primary']")]
topic_urls = [f"{github_url}{x.get('href')}" for x in topics_soup.select(selector="div a[class='no-underline flex-1 d-flex flex-column']")]

# print(topic_names)
# print(topic_urls)

a_topic_url = topic_urls[0]
a_topic_response = requests.get(a_topic_url)
print(a_topic_response.status_code)
a_topic_soup = BeautifulSoup(a_topic_response.text,"html.parser")
user_names = [x.getText().strip("\n\t ") for x in a_topic_soup.select(selector="a[class='Link']")]
repo_urls = [f"{github_url}{x.get("href")}" for x in a_topic_soup.select("a[class='Link text-bold wb-break-word']")]
repo_names = [x.getText().strip("\n\t ") for x in a_topic_soup.select("a[class='Link text-bold wb-break-word']")]
stars = [x.getText() for x in a_topic_soup.select("span[class='Counter js-social-count']")]

# print(user_names)
# print(repo_names)
# print(repo_urls)
# print(stars)
# print(len(user_names), len(repo_names), len(repo_urls), len(stars))

for topic,topic_name in zip(topic_urls, topic_names):
    a_topic_url = topic
    a_topic_response = requests.get(a_topic_url)
    print(a_topic_response.status_code)
    a_topic_soup = BeautifulSoup(a_topic_response.text,"html.parser")
    user_names = [x.getText().strip("\n\t ") for x in a_topic_soup.select(selector="a[class='Link']")]
    repo_urls = [f"{github_url}{x.get("href")}" for x in a_topic_soup.select("a[class='Link text-bold wb-break-word']")]
    repo_names = [x.getText().strip("\n\t ") for x in a_topic_soup.select("a[class='Link text-bold wb-break-word']")]
    stars = [x.getText() for x in a_topic_soup.select("span[class='Counter js-social-count']")]

    with open(f"Day47/csvs/{topic_name}.csv", "w") as f:
        f.write("Repo Name, User Name, Stars, Repo URL\n")
        for repo_name,user_name, star, repo_url in zip(repo_names,user_names,stars,repo_urls):
            f.write(f"{repo_name},{user_name},{star}, {repo_url}\n")

