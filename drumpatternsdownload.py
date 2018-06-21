import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
import re

url = 'http://media.afromix.org/music/midi/drum_patterns/'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
links = page_soup.findAll("li")


for link in links[1:]:
    x = str(link)
    y = x.find('/')
    newstr = x[13:y]

    folder = newstr.upper()
    newurl = url + newstr
    uClient = uReq(newurl)
    page_html = uClient.read()
    page_soup = soup(page_html, 'html.parser')
    uClient.close()
    files = page_soup.findAll("a", href=re.compile(".MID$"))
    lfiles = page_soup.findAll("a", href=re.compile(".mid$"))
    allfiles = files + lfiles

    for file in allfiles:
        e = str(file)
        g = e.find('">')
        h = e[9:g]
        fullPath = './' + folder + '/' + h
        if not os.path.exists(folder):
            os.makedirs(folder)
        print("Downloading " + newstr + "/" + h)
        print("----------")
        r = requests.get(newurl)
        with open(fullPath, "wb") as code:
            code.write(r.content)