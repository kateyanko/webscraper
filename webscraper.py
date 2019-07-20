import requests
import re
from bs4 import BeautifulSoup

page = requests.get('https://www.agentquery.com/search.aspx?l=1')
soup = BeautifulSoup(page.content, 'html.parser')


paragraphs=soup.findAll('p')
for info_cards in paragraphs:
	name=info_cards.findAll(class_='result')
	email=info_cards.findAll('span', id=re.compile('Email'))
# #THIS IS WORKING, but we have to figure out how to print the text found after it. 
# 	genres=info_cards.findAll(text=re.findall('FICTION GENRES',str(paragraphs)))
	# for titles in genres.find_next_sibling(text=True):
	# 	print titles.string

	websites=info_cards.findAll('a', href=True, id=re.compile('lnkAgency'))
	for i in name:
		print i.text
	for j in email:
		print j.text
	# for k in genres:
	# 	print k
	for l in websites:
		print(l.get('href'))
	
