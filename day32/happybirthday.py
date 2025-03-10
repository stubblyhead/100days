import smtplib

with open('totallynotpasswords.txt') as data:
    line = data.read()
    email,pw = line.split(',')

dest_email = email.replace('@', '+test@')

with smtplib.SMTP("smtp.gmail.com", port=587) as cxn:
    cxn.starttls()
    cxn.login(user=email,password=pw)
    cxn.sendmail(
        from_addr=email,
        to_addrs=dest_email,
        msg="Subject:hello thar\n\nthis is an email"
    )
