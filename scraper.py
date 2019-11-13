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

    # appt_url = 'https://app.timetrade.com/tc/ReceptionistMakeAppointmentDayTimeFrame.do?org.apache.struts.taglib.html.TOKEN=9db46763b721816d9ec6f0fe82071526&method=modify&min=0&hour=0&activity=4&resource=-1&showAppointments=&appointmentId=&apptGroupType=1&frame=true&setDay=false&grid=minus&cmd=save&process=client&process2=client&entry=&level=&urlstring=spainconsulchicago&step=IntegratedQueryInterface&year=2019&month=10&day=14'

    # TODO: check if this token needs to be dynamically chosen
    appt_url = 'https://app.timetrade.com/tc/ReceptionistMakeAppointmentDayTimeFrame.do?org.apache.struts.taglib.html.TOKEN=3af9008f125708200262a56185985435&method=nextFrame&selectedProgramName=+Visa+Application++Program&selectedActivityName=+Student+Visa&selectedResourceName=Any+Resource&durationLabel=20+mins&copyOfProgram=-32767&copyOfActivity=-32767&copyOfResource=-32767&copyOfDuration=-1&copyOfAttendees=1&showAppointments=&apptGroupType=1&frame=true&showAvailable=first&resetQuery=true&cmd=save&process=client&process2=client&entry=&level=&urlstring=spainconsulchicago&step=IntegratedQueryInterface&resource=-1&program=1&activity=4&setupTime=0&duration=20&attendees=1&clientTimeZone=America%2FChicago'

    page = self.session.get(appt_url);
    print(page)
    print(page.status_code)
    if page.status_code == 200:
      self.content = page.content
      # print(self.content)
    else:
      raise Exception('page could not be accessed!')

    print(self.session)

    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify)
    
    # payload = {
    #   "userName": "<REDACTED>",
    #   "password": "<REDACTED>",
    # }
    # login_result = self.session.post(login_url, data=payload, headers=dict(referrer=login_url))
    # print(login_result)
    # print(login_result.content

scraper = Scraper()
scraper.download()

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
#
#   # import HTMLSession from requests_html
# from requests_html import HTMLSession
#
# # def main():
#   # create an HTML Session object
# session = HTMLSession()
#
# print('Hello!')
#
# login_url = 'https://app.timetrade.com/tc/login.do?cmd=direct&process=login&process2=login&entry=Select&level=&urlstring=spainconsulchicago&step=Signin&method=login&userName=<REDACTED>&password=<REDACTED>'
#
# # Use the object above to connect to needed webpage
# resp = session.get(login_url)
# print(resp.status_code)
# # Run JavaScript code on webpage
# resp.html.render();
#
# print(resp.html.html)
#
# appt_url = 'https://app.timetrade.com/tc/ReceptionistMakeAppointmentDayTimeFrame.do?org.apache.struts.taglib.html.TOKEN=9db46763b721816d9ec6f0fe82071526&method=modify&min=0&hour=0&activity=4&resource=-1&showAppointments=&appointmentId=&apptGroupType=1&frame=true&setDay=false&grid=minus&cmd=save&process=client&process2=client&entry=&level=&urlstring=spainconsulchicago&step=IntegratedQueryInterface&year=2019&month=10&day=14'
# appt_url = 'https://app.timetrade.com/tc/ReceptionistMakeAppointmentDayTimeFrame.do?org.apache.struts.taglib.html.TOKEN=3af9008f125708200262a56185985435&method=nextFrame&selectedProgramName=+Visa+Application++Program&selectedActivityName=+Student+Visa&selectedResourceName=Any+Resource&durationLabel=20+mins&copyOfProgram=-32767&copyOfActivity=-32767&copyOfResource=-32767&copyOfDuration=-1&copyOfAttendees=1&showAppointments=&apptGroupType=1&frame=true&showAvailable=first&resetQuery=true&cmd=save&process=client&process2=client&entry=&level=&urlstring=spainconsulchicago&step=IntegratedQueryInterface&resource=-1&program=1&activity=4&setupTime=0&duration=20&attendees=1&clientTimeZone=America%2FChicago'
#
# # print(resp.html)
# # resp.html.render()
#
# resp = session.get(appt_url);
# print(resp.status_code)
# resp.html.render()
# print(resp.html.html)
