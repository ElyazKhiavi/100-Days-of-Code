from bs4 import BeautifulSoup
with open("./website.html", "r") as f:
    content = f.read()
# end append file



soup = BeautifulSoup(content, 'html.parser')
print(soup)