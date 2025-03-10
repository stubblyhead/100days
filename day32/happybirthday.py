import smtplib
import datetime as dt

with open('totallynotpasswords.txt') as data:
    line = data.read()
    email,pw = line.split(',')

with open('birthdays.csv') as data:
    _ = data.readline()
    people = list(map(lambda s: s.split(','), data.readlines()))

letters = []
for i in range(1,4):
    with open(f'letter_templates/letter_{i}.txt') as data:
        letters.append(data.read())

now = dt.datetime.now()



with smtplib.SMTP("smtp.gmail.com", port=587) as cxn:
    cxn.starttls()
    cxn.login(user=email,password=pw)
    cxn.sendmail(
        from_addr=email,
        to_addrs=dest_email,
        msg="Subject:hello thar\n\nthis is an email"
    )
