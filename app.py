import mechanize
from BeautifulSoup import BeautifulSoup
response = mechanize.urlopen("https://www.indeed.com/jobs?q=(python%20or%20javascript)&l=San%20Francisco%20Bay%20Area%2C%20CA&jt=fulltime&rbl=San%20Francisco%2C%20CA&jlid=6cf5e6d389fd6d6b&ts=1507163367492&rq=1&fromage=last")
print(response.read())
regex = '/href\w/g'
m = response.search(regex)
print m
