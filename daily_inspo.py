import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from twilio.rest import Client
import time


# Account SID from twilio.com/console
account_sid = "ACc4dad3733a3552567bff7a53caaeb429"
# Auth Token from twilio.com/console
auth_token  = "d9c34a5c90cdb9d5935c89603c996de6"


if __name__ == '__main__':
    db_client = MongoClient
    client = Client(account_sid, auth_token)
    response = requests.get("https://www.eduro.com/")
    soup = BeautifulSoup(response.content, "lxml")

    article = soup.find('div',class_='article')
    post_quotes = article.p.text

    post_authors = soup.find('p', class_='author').text
    
    if soup.find('post_authors') is None:
<<<<<<< HEAD
        fromNumber = '+16314029977'
        toNumber = '+16318735203'
        message = (post_quotes + "\n" + post_authors)
        client.messages.create(to=toNumber, from_=fromNumber, body=message)
=======
        client.messages.create (
            from_= '+16314029977'
            to= '+16318735203'
            body= post_quotes + "\n" + post_authors
            )
>>>>>>> 9d4e59aaf50ec4bc5efc0409dcacb35232964aa5


