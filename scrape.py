import nltk
    #gets the libraries we need
from bs4 import BeautifulSoup
    #inside bs4 is this software to pull
from urllib import request
    #comes with python, but won't always be open, have to activate it

url = "https://github.com/humanitiesprogramming/scraping-corpus"
    #store the url we are using

html = request.urlopen(url).read()
    #using that url, get the HTML from it

soup = BeautifulSoup(html, "lxml")

#print(soup.text)
    # took the url and turned into a soup object
our_text = soup.text
#soup.find_all('a')[0:10]
links = soup.find_all('a')[0:10]

#print(our_text[0:2000])
#print(soup.text.replace('\n', " "))

links_html = soup.select('td.content a')
this_link = links_html[0]

#print(this_link['href'])

urls = []
for link in links_html:
    to_append = (link['href']). replace('blob/', '')
#gave us the url for each of the txt files on the original pages
    urls.append("https://raw.githubusercontent.com" + to_append)

test_url = urls[3]
corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
    print("scraping" + url)
print(len(corpus_texts))
print(len(corpus_texts[0]))

this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
print(process_this_text[0:20])
print(nltk.FreqDist(process_this_text).most_common(50))
