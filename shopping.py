import bs4 as bs
import urllib.request

a = input ('enter the item to be searched :')

#items from flipkart
sauce = urllib.request.urlopen('https://www.flipkart.com/search?q='+a+'&marketplace=FLIPKART&otracker=start&as-show=off&as=off').read()
soup = bs.BeautifulSoup(sauce,'lxml')

for url in soup.find_all('a', class_='Zhf2z-' or '_31qSD5'):
    print (url.get('href'))


#items from amazon
sauce1 = urllib.request.urlopen('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+a).read()
soup1 = bs.BeautifulSoup(sauce1,'lxml')

for url in soup1.find_all('a', class_='a-link-normal a-text-normal'):
    print (url.get('href'))