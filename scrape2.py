import requests
import re
from bs4 import BeautifulSoup
html = requests.get("http://dataspace.princeton.edu/jspui/browse?type=graduation&order=DESC&rpp=100&value=2014").text
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class':'miscTable'})
links = []
for link in table.find_all('a', href=True):
    links.append(link['href'])

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
print articles