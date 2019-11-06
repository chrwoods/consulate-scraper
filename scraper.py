from bs4 import BeautifulSoup
from lxml import html
import requests

class Scraper:
  def __init__(self):
    self.soup = None
    self.content = None
    self.session = requests.session()

  def download(self):
    login_url = 'https://app.timetrade.com/tc/login.do?cmd=direct&process=login&process2=login&entry=Select&level=&urlstring=spainconsulchicago&step=Signin&method=login&userName=<REDACTED>&password=<REDACTED>'
    page = self.session.get(login_url);
    print(page)
    if page.status_code == 200:
      self.content = page.content
      # print(self.content)
    else:
      raise Exception('page could not be accessed!')
    
    appt_url = 'https://app.timetrade.com/tc/ReceptionistManageAppointmentClient.do?org.apache.struts.taglib.html.TOKEN=50721ae5a23c77d8a7cdc542fef9382b&method=out&compound=&appointmentsSort=&confirmationNumber=&appointmentId=&waitList=false&view=2&cancellation=false&cmd=tab&process=client&process2=client&entry=MakeAppointments&level=&urlstring=spainconsulchicago&step=ReceptionistManageAppointmentClient'

    page = self.session.get(appt_url);
    print(page)
    if page.status_code == 200:
      self.content = page.content
      print(self.content)
    else:
      raise Exception('page could not be accessed!')

    self.session.
    # payload = {
    #   "userName": "<REDACTED>", 
    #   "password": "<REDACTED>",
    # }
    # login_result = self.session.post(login_url, data=payload, headers=dict(referrer=login_url))
    # print(login_result)
    # print(login_result.content)

def main():
  scrape = Scraper()
  scrape.download()

#   # import HTMLSession from requests_html
# from requests_html import HTMLSession
 
# def main():
#   # create an HTML Session object
#   session = HTMLSession()
  
#   # Use the object above to connect to needed webpage
#   resp = session.get("https://app.timetrade.com/tc/login.do?cmd=direct&process=login&process2=login&entry=Select&level=&urlstring=spainconsulchicago&step=Signin&method=login&userName=<REDACTED>&password=<REDACTED>")
#   print(resp.status_code)
#   # Run JavaScript code on webpage
#   resp.html.render()

#   print(resp.html)
