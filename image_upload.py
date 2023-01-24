import os
import requests

from auth import *

class ImageTweet(object):

    def __init__(self, filename):
		
        '''
        Defines image tweet properties
        '''
        self.image_filename = filename
        self.total_bytes = os.path.getsize(self.image_filename)
        self.media_id = None
        self.processing_info = None
        self.oauth = getTwitterAuth()
        self.media_endpoint_url = 'https://upload.twitter.com/1.1/media/upload.json'
        self.post_tweet_url = 'https://api.twitter.com/1.1/statuses/update.json'

    def tweet(self):
        '''
        Publishes Tweet with attached image
        '''
        image_path = self.image_filename
        with open(image_path, "rb") as image_file:
            files = {"media": image_file}
            req = requests.post(self.media_endpoint_url, 
                                files=files, auth=self.oauth)
            self.media_id = req.json()["media_id"]

        status = self.image_filename.split("_")[0]

        request_data = {
            'status': 'Oshi no Ko, Chapter ' + status,
            'media_ids': self.media_id
        }
        req = requests.post(self.post_tweet_url, data=request_data, auth=self.oauth)
        print(req.json())
        os.remove(self.image_filename)