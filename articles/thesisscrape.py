# requires requests and beautifulsoup4

import requests
from bs4 import BeautifulSoup
html = requests.get("http://dataspace.princeton.edu/jspui/browse?type=graduation&order=DESC&rpp=200000&value=2014").text
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class':'miscTable'})
data = []
for tr in table.find_all('tr')[1:]:
    tds = tr.find_all('td')
    data.append([ele.text.replace("\r\n", " ").encode('ascii','ignore') for ele in tds])


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
for thesis in data:
	# format date
	datearr = thesis[0].split("-")
	date = datetime.date(datearr[2], months[datearr[1]], datearr[0])
	title = thesis[1]
	author = thesis[2]
	a = Article(title=title, author=author, pub_date=date)
	a.save()