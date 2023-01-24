import os

from dotenv import load_dotenv

from requests_oauthlib import OAuth1

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def getTwitterAuth():

    load_dotenv()

    # Set the Twitter API credentials
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    twitter_auth = OAuth1(CONSUMER_KEY,
                          client_secret=CONSUMER_SECRET,
                          resource_owner_key=ACCESS_TOKEN,
                          resource_owner_secret=ACCESS_TOKEN_SECRET)

    return twitter_auth


def getGoogleAuth():

    gauth = GoogleAuth()
    drive_auth = GoogleDrive(gauth)

    return drive_auth
