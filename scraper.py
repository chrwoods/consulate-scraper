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
    # print(page)
    if page.status_code == 200:
      self.content = page.content
      # print(self.content)
    else:
      raise Exception('page could not be accessed!')
    
    # appt_url = 'https://app.timetrade.com/tc/ReceptionistManageAppointmentClient.do?org.apache.struts.taglib.html.TOKEN=50721ae5a23c77d8a7cdc542fef9382b&method=out&compound=&appointmentsSort=&confirmationNumber=&appointmentId=&waitList=false&view=2&cancellation=false&cmd=tab&process=client&process2=client&entry=MakeAppointments&level=&urlstring=spainconsulchicago&step=ReceptionistManageAppointmentClient'

    appt_url = 'https://app.timetrade.com/tc/ReceptionistMakeAppointmentDayTimeFrame.do?org.apache.struts.taglib.html.TOKEN=9db46763b721816d9ec6f0fe82071526&method=modify&min=0&hour=0&activity=4&resource=-1&showAppointments=&appointmentId=&apptGroupType=1&frame=true&setDay=false&grid=minus&cmd=save&process=client&process2=client&entry=&level=&urlstring=spainconsulchicago&step=IntegratedQueryInterface&year=2019&month=10&day=14'

    page = self.session.get(appt_url);
    print(page)
    if page.status_code == 200:
      self.content = page.content
      print(self.content)
    else:
      raise Exception('page could not be accessed!')

    print(self.session)
    # payload = {
    #   "userName": "<REDACTED>", 
    #   "password": "<REDACTED>",
    # }
    # login_result = self.session.post(login_url, data=payload, headers=dict(referrer=login_url))
    # print(login_result)
    # print(login_result.content)

# def main():
#   scrape = Scraper()
#   scrape.download()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# user_name = "YOUR EMAILID"
# password = "YOUR PASSWORD"
# driver = webdriver.Firefox()
# driver.get("https://www.facebook.com")
# element = driver.find_element_by_id("email")
# element.send_keys(user_name)
# element = driver.find_element_by_id("pass")
# element.send_keys(password)
# element.send_keys(Keys.RETURN)
# element.close()

  # import HTMLSession from requests_html
from requests_html import HTMLSession
 
def main():
  # create an HTML Session object
  session = HTMLSession()
  
  # Use the object above to connect to needed webpage
  resp = session.get("https://app.timetrade.com/tc/login.do?cmd=direct&process=login&process2=login&entry=Select&level=&urlstring=spainconsulchicago&step=Signin&method=login&userName=<REDACTED>&password=<REDACTED>")
  print(resp.status_code)
  # Run JavaScript code on webpage

  print(resp.html)
  resp.html.render()

  print(resp.html)
