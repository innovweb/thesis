# requires requests, re, and beautifulsoup4
import requests
import re
from bs4 import BeautifulSoup
num_to_scrape = "1189"
year = "2014"
html = requests.get("http://dataspace.princeton.edu/jspui/browse?type=graduation&order=DESC&rpp="+num_to_scrape+"&value="+year).text
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
    else:
        articles[count]["abstract"] = ""
    pdf = soup.find("meta", {"name":"citation_pdf_url"})
    if (pdf):
        articles[count]["pdf"] = pdf["content"].replace("\r\n", " ").encode('ascii','ignore')
    else:
        articles[count]["pdf"] = ""
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

# process the stuff!
for article in articles:
    # format date
    datearr = article["date"].split("-")
    for i in range(3): # convert to ints
        datearr[i] = int(datearr[i])
    date = datetime.date(datearr[0], datearr[1], datearr[2])
    # rest of info
    title = article["title"]
    author = article["author"]
    department = article["department"]
    abstract = article["abstract"]
    link = article["pdf"]
    # add new article to database
    a = Article(title=title, author=author, pub_date=date, department=department, abstract=abstract, article_link=link)
    a.save()