from bs4 import BeautifulSoup
import urllib2
import time
today = int(time.strftime("%d"))
print today
recentDays = [today, today-1,today-2]
editorSite= urllib2.urlopen('http://www.publishersmarketplace.com/jobs/')
siteHtml = editorSite.read()
editorSite.close()
soup = BeautifulSoup(siteHtml,"lxml")
#print soup
headerLines = soup.find_all(class_="toplineL")
dateLines = soup.find_all(class_="toplineR")
#print headerLines
#print dateLines
for l in range(0,len(headerLines)):
  #  print l
    if(True):
        print headerLines[l].get_text()
        print dateLines[l].get_text()


