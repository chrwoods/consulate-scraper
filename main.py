from scraper import Scraper
from sms import Texter
from datetime import datetime

scraper = Scraper()
scraper.login()
header = scraper.get_earliest_appointment_header()

if header:
    if '2019' in header:
        texter = Texter()
        texter.send('Open appointment found in range: ' + header + '!')
    # Send a daily alert at 8 am so I know that the service is still running.
    elif datetime.now().strftime('%H') == '8':
        texter = Texter()
        texter.send('DAILY UPDATE: '
                    'Earliest appointment is in range: ' + header + '.')
