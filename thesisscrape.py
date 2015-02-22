import requests
from bs4 import BeautifulSoup
html = requests.get("http://dataspace.princeton.edu/jspui/browse?type=graduation&order=DESC&rpp=200000&value=2014").text
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class':'miscTable'})
data = []
for tr in table.find_all('tr')[1:]:
    tds = tr.find_all('td')
    data.append([ele.text.replace("\r\n", " ").encode('ascii','ignore') for ele in tds])
print data