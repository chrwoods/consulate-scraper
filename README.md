# consulate-scraper
Short python script to scrape the Spanish consulate's appointment website to find the earliest range of open appointments, written by Christopher Woods.

## Configuration

All configuration (login, phone numbers, etc.) should be placed in a `secrets.py` file in the main directory, which for obvious security reasons has not been included in the git repository.

The `secrets.py` file should be formatted as:
```$xslt
USERNAME = 'username'
PASSWORD = 'password'
TO_NUMBER = '+15558675309'
FROM_NUMBER = '+17732025000'
TWILIO_SID = 'AC------'
TWILIO_AUTH_TOKEN = '----------'
```

`TWILIO_SID` and `TWILIO_AUTH_TOKEN` refer to the tokens given from Twilio, the SMS messaging service that this script uses to send texts when an open appointment is found.

As such, the `TO_NUMBER` is the number that you want the SMS text message sent to, while the `FROM_NUMBER` is also given by Twilio.

`USERNAME` and `PASSWORD` refer to the login credentials for the Spanish consulate website.

## Running

Required packages:

- `bs4` for webscraping with BeautifulSoup
- `requests` to query the website
- `twilio` to send SMS text messages

Once those are installed with something like `pip`, and the `secrets.py` file is set up, the program can be run with `python main.py`.

Ideally this should be set up to run on a cron job, with a crontime something like `*/10 * * * *` (set to run every 10 minutes). 

If this is run on a cron job, it is set up to send out daily alerts at 8 AM and 6 PM to tell the user that the service is still running, along with sending out a text every time an appointment is found some time in 2019.