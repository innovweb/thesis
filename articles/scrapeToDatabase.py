# requires requests, re, and beautifulsoup4
import requests
import re
from bs4 import BeautifulSoup
html = requests.get("http://dataspace.princeton.edu/jspui/browse?type=graduation&order=DESC&rpp=5&value=2014").text
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class':'miscTable'})
# links to search through
links = []
for link in table.find_all('a', href=True):
    links.append(link['href'])
# get all article information
articles = [dict() for list in links]
count = 0
for link in links:
    html = requests.get("http://dataspace.princeton.edu/" + link).text
    soup = BeautifulSoup(html)
    articles[count]["department"] = soup.find('td', text=re.compile("Department")).find_next_siblings()[0].text.replace("\r\n", " ").encode('ascii','ignore')
    articles[count]["author"] = soup.find("meta", {"name":"DC.contributor"})["content"].replace("\r\n", " ").encode('ascii','ignore')
    articles[count]["title"] = soup.find("meta", {"name":"DC.title"})["content"].replace("\r\n", " ").encode('ascii','ignore')
   
    abstract = soup.find("meta", {"name":"DCTERMS.abstract"})
    if (abstract):
        articles[count]["abstract"] = abstract["content"].replace("\r\n", " ").encode('ascii','ignore')
    
    pdf = soup.find("meta", {"name":"citation_pdf_url"})
    if (pdf):
        articles[count]["pdf"] = pdf["content"].replace("\r\n", " ").encode('ascii','ignore')
    
    articles[count]["date"] = soup.find("meta", {"name":"citation_date"})["content"].replace("\r\n", " ").encode('ascii','ignore')
    count += 1

# set up Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
import django
django.setup()

from articles.models import Article
import datetime
import calendar

# create dictionary mapping months to ints
months = dict((v,k) for k,v in enumerate(calendar.month_abbr))

# process the stuff
for article in articles:
	print(article)
	# format date
	datearr = article["date"].split("-")
	date = datetime.date(datearr[2], months[datearr[1]], datearr[0])
	# rest of info
	title = article["title"]
	author = article["author"]
	department = article["department"]
	abstract = article["abstract"]
	link = article["pdf"]
	# add new article to database
	a = Article(title=title, author=author, pub_date=date, department=department, abstract=abstract, article_link=link)
	a.save()