from bs4 import BeautifulSoup
import requests
import secrets


class Scraper:
    def __init__(self):
        self.session = requests.session()

    def login(self):
        login_url = 'https://app.timetrade.com/tc/login.do?cmd=direct&process=login&process2=login&entry=Select&level=&urlstring=spainconsulchicago&step=Signin&method=login&userName={}&password={}' \
            .format(secrets.USERNAME, secrets.PASSWORD)

        page = self.session.get(login_url)
        if page.status_code != 200:
            raise Exception('Found status code {} while attempting to login.'.format(page.status_code))

    def get_earliest_appointment_header(self):
        appt_url = 'https://app.timetrade.com/tc/ReceptionistMakeAppointmentDayTimeFrame.do?method=nextFrame&selectedProgramName=+Visa+Application++Program&selectedActivityName=+Student+Visa&selectedResourceName=Any+Resource&durationLabel=20+mins&copyOfProgram=-32767&copyOfActivity=-32767&copyOfResource=-32767&copyOfDuration=-1&copyOfAttendees=1&showAppointments=&apptGroupType=1&frame=true&showAvailable=first&resetQuery=true&cmd=save&process=client&process2=client&entry=&level=&urlstring=spainconsulchicago&step=IntegratedQueryInterface&resource=-1&program=1&activity=4&setupTime=0&duration=20&attendees=1&clientTimeZone=America%2FChicago'

        page = self.session.get(appt_url)
        if page.status_code != 200:
            raise Exception('Found status code {} while attempting to get appointments.'.format(page.status_code))

        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find_all('font', class_='f24b')[0].get_text().strip()