import requests as rq
from bs4 import BeautifulSoup
url=input('Enter the url: ')
if ('https' or 'http') in url:
    data=rq.get(url)
else:
    data= rq.get('https://'+ url)
sp= BeautifulSoup(data.text,'html.parser')
links=[]
for link in sp.find_all('a'):
    links.append(link.get('href'))

with open('fetched links.txt','a') as saved:
    print(links[:10],file=saved)
        
                
