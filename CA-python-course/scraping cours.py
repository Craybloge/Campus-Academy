from bs4 import BeautifulSoup
import requests
import csv
citations= []
for i in range (1,11):
    url= "http://quotes.toscrape.com/page/{}/".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for i in soup.find_all('span', class_="text"):
        txt = i.get_text()
        txt=txt.replace("“", "")
        txt=txt.replace("”", "")
        txt=txt.replace("\"", "")
        txt=txt.replace("′", "'")
        citations.append(txt)

print(citations)
with open('citation.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter =',')
    writer.writerow(citations)

    


# database sql
