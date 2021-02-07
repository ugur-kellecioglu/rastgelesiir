import requests
import random
from bs4 import BeautifulSoup

class Poem:
    def __init__(self, title="", author="", poem=""):
        self.title = title
        self.author = author
        self.poem = poem
    
    def setAll(self):
        r = requests.get(self.poems())
        allHTML = BeautifulSoup(r.content, "lxml")
        self.title = allHTML.find_all("div", "topic")

        titleAndAuthor = BeautifulSoup(str(self.title[0]), 'lxml')
        self.title = titleAndAuthor.find("a").get_text()
        self.author = titleAndAuthor.find("div", "author").get_text()
        self.author = self.author[self.author.find(":") + 2:]

        poemText = allHTML.find("div", "text").get_text().strip()
        poemAll = ""
        for letter in poemText:
            if(letter.isupper()):
                poemAll += "" + letter
            else:
                poemAll +=  letter

        self.poem = poemAll

    def directRandomPage(self):
        return random.randint(0,5450)

    def poems(self):
        url = "http://siir.sitesi.web.tr/siirler-"+str(self.directRandomPage())+".html"
        r = requests.get(url)
        allHTML = str(BeautifulSoup(r.content, "lxml").find_all("div", "siir"))
        allHTML = BeautifulSoup(allHTML, "lxml").find_all("a")
        return allHTML[4].get('href')
        
p = Poem()
p.setAll()
print("Şair: " + p.author + "\n\n" + "Başlık: " + p.title + "\n\n" + p.poem)