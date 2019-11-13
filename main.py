from scraper import Scraper
from sms import Texter
from datetime import datetime

scraper = Scraper()
scraper.login()
header = scraper.get_earliest_appointment_header()

if header:
    print(header)
    if '2019' in header:
        texter = Texter()
        texter.send('Open appointment found in range: ' + header + '!')
    # Send daily alerts at 8:00 am and 6:00 pm so I know that the service is still running.
    elif '8:00' in datetime.now().strftime('%H:%M'):
        texter = Texter()
        texter.send('DAILY UPDATE: '
                    'Earliest appointment is in range: ' + header + '.')
