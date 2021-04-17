from bs4 import BeautifulSoup as BSHTML
#import urllib.request
import requests


#with urllib.request.urlopen("https://downloaderi.com/download.php?url=https://www.tiktok.com/@swapatkar/video/6844106037922893057") as url:
#    page = url.read()
page=requests.get("https://downloaderi.com/download.php?url=https://www.tiktok.com/@swapatkar/video/6842266075669777665").text    

soup = BSHTML(page)
    
   

my_data = soup.find_all("a", id= "downloadlink")
for x in my_data:
    my_href = x.get("href")
    print(my_href)

  