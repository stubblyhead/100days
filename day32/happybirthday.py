import smtplib
import datetime as dt
from random import choice

with open('totallynotpasswords.txt') as data:
    line = data.read()
    email,pw = line.split(',')

with open('birthdays.csv') as data:
    _ = data.readline() # throw out headers
    people = list(map(lambda s: s.strip().split(','), data.readlines()))

letters = []
for i in range(1,4):
    with open(f'letter_templates/letter_{i}.txt') as data:
        letters.append(data.read())

now = dt.datetime.now()
cur_month = str(now.month)
cur_day = str(now.day)

for p in people:
    if cur_month == p[3] and cur_day == p[4]:
        letter = choice(letters)
        letter = letter.replace('[NAME]',p[0])
        with smtplib.SMTP("smtp.gmail.com", port=587) as cxn:
            cxn.starttls()
            cxn.login(user=email,password=pw)
            cxn.sendmail(
                from_addr=email,
                to_addrs=p[1],
                msg=f"Subject:happy birthday!\n\n{letter}"
            )
