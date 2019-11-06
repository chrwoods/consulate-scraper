from bs4 import BeautifulSoup
import requests

class Scraper:
  def __init__(self):
    self.soup = None
    self.content = None

  def download(self):
    page = requests.get('https://app.timetrade.com/tc/login.do?url=spainconsulchicago');
    print(page)
    if page.status_code == 200:
      self.content = page.content
      print(self.content)
    else:
      raise Exception('Page could not be accessed: ' + page.status_code)
