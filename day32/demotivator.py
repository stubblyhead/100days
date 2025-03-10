import smtplib
import datetime as dt
from random import choice

with open('totallynotpasswords.txt') as data:
    line = data.read()
    email,pw = line.split(',')

with open('quotes.txt') as data:
    quotes = data.readlines()

dest_email = email.replace('@', '+test@')

now = dt.datetime.now()

if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as cxn:
        cxn.starttls()
        cxn.login(user=email,password=pw)
        cxn.sendmail(
            from_addr=email,
            to_addrs=dest_email,
            msg=f"Subject:mondays ACK\n\n{choice(quotes)}"
        )