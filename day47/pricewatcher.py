from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
import re
import dotenv
import os

dotenv.load_dotenv('.env')
email = os.getenv('EMAIL')
pw = os.getenv('PASSWORD')

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
"Priority": "u=0, i",
"Sec-Ch-Ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": '"Windows"',
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
}

endpoint_url = 'https://www.amazon.com/dp/B075CYMYK6'
response = requests.get(url=endpoint_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

price_div = soup.find(name='div', id='corePriceDisplay_desktop_feature_div')
price = float(price_div.find(name='span').get_text().strip()[1:])
product_title = soup.find(id='productTitle').get_text().strip()
product_title = re.sub(r'\s+', ' ', product_title)

if price < 100:
    letter = f"""{product_title} is really cheap right now, only ${price}.\n\nBuy here: {endpoint_url}
"""
    msg = MIMEText(f'{letter}'.encode('utf-8'), _charset='utf-8')
    msg['Subject'] = 'cheap instant pot alert'
    with smtplib.SMTP('smtp.gmail.com', port=587) as cxn:
        cxn.starttls()
        cxn.login(user=email,password=pw)
        cxn.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=msg.as_bytes()
        )