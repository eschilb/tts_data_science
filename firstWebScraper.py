from bs4 import BeautifulSoup

soup = BeautifulSoup(open("files/43rd-congress.html"), features="lxml")

#print(soup.prettify())

links = soup.find_all('a')

for link in links:
    print(link)