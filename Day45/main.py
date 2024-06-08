from bs4 import BeautifulSoup
# import lxml

with open("Day45/website.html",encoding="UTF-8") as f:
    contents = f.read()


soup = BeautifulSoup(contents,"html.parser") # for xml =import lxml and use "lxml"

print(soup.title)
print(soup.title.name, soup.title.string)
print(soup.a)  # first a tag
print(soup.li) # first li tag

# print(soup.prettify())
# print(soup)

all_anchor_tags = soup.find_all(name='a')
all_anchor_names = [x.getText() for x in all_anchor_tags]
all_links = [x.get("href") for x in all_anchor_tags]
print(all_anchor_tags)
print(all_anchor_names)
print(all_links)

heading = soup.find(name="h1",id="name")  # finding based on attributes
print(heading)
section_heading = soup.find(name="h3",class_="heading")  # notice _ in var name 
print(section_heading)


# to get more specific element based on css selector:

company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)
headings = soup.select(selector=".heading")
print(headings)

