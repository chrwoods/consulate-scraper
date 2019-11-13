from scraper import Scraper
from sms import Texter

scraper = Scraper()
scraper.login()
header = scraper.get_earliest_appointment_header()

if header:
    texter = Texter()
    texter.send(header)