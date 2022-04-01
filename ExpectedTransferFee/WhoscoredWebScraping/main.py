from bs4 import BeautifulSoup
import requests
import selenium




URL = 'https://www.whoscored.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


results = soup.find(id="overall-top-players-overall-content")
print(results.prettify())
