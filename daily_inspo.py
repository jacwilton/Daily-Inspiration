import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from twilio.rest import Client
from datetime import datetime
from threading import Timer
from numpy import *
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find workbook by name and open first sheet
sheet = client.open('daily_inspo').sheet1


x=datetime.today()
y=x.replace(day=x.day+1, hour=15, minute=57, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1



# Account SID from twilio.com/console
account_sid = "ACc4dad3733a3552567bff7a53caaeb429"
# Auth Token from twilio.com/console
auth_token  = "d9c34a5c90cdb9d5935c89603c996de6"
service_sid = "MG5bcd49680626fc4e0d5ee41079ba9b6d"



if __name__ == '__main__':
    db_client = MongoClient
    client = Client(account_sid, auth_token)
    response = requests.get("https://www.eduro.com/")
    soup = BeautifulSoup(response.content, "lxml")

    article = soup.find('div',class_='article')
    post_quotes = article.p.text

    post_authors = soup.find('p', class_='author').text

def send_text():
    if soup.find('post_authors') is None:
        for num in range (2,4):
            numbers = sheet.acell('a' + str(num)).value
            if not numbers:
                print ("no number")
        else:
                client.messages.create (
                            from_= service_sid,
                            to= "+" + numbers,
                            body= post_quotes + "\n" + post_authors
                                    )

t = Timer(secs,send_text)
t.start()

