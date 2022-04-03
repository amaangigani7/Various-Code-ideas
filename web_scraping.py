import requests
import bs4

# result = requests.get("http://www.example.com")
# # print(result.text)
#
# soup = bs4.BeautifulSoup(result.text, 'lxml')
#
# print(soup.select('p'))
# site_para = soup.select('title')
# print(site_para[0].getText())
# res = requests.get('https://en.wikipedia.org/wiki/Charles_Babbage')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# first_item = soup.select('ul')[0]
#
# for item in soup.select('t'):
#     print(item.text)

# res = requests.get('https://en.wikipedia.org/wiki/Charles_Babbage')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# images = soup.select('img')
# print(images[1])
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# products = soup.select('.product_pod')
# example = products[0]
# # if 'star-rating Three' in str(example):
# print(example.select('.star-rating.Three'))
# print(example.select('a')[1]['title'])

two_star_titles = []

for n in range(1, 11):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)
