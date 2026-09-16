from bs4 import BeautifulSoup



with open("./index.html", "r") as f:
    content = f.read()
# end append file


soup = BeautifulSoup(content, "html.parser")
print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)


for anchor in all_anchor_tags:
    href = anchor.get("href")
    print(href)

h1 = soup.find(name="h1")
print(h1.string)

culture = soup.find(name="section", id="culture")
print(culture)


### Select and Select One

# select one get's the first matching
# select sends that match

article_text = soup.select_one(selector="article p")
print(article_text.string)

all_article_text = soup.select(selector='article p')
for i in all_article_text:
    print(i.string)

