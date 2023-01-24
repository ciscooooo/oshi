import time
import requests

from image_upload import ImageTweet
from video_upload import VideoTweet
from utilities import *

if __name__ == '__main__':

	while(True):
    
		file = getRandomFile()

		if file['extension'] == 'mp4':
			videoTweet = VideoTweet(file['title'])
			videoTweet.tweet()

		if file['extension'] == 'png':
			imageTweet = ImageTweet(file['title'])
			imageTweet.tweet()


		time.sleep(14.5*60)
		try:
			r = requests.head("https://oshi.onrender.com")
			print(r.status_code)
		except requests.ConnectionError:
			print("failed to connect")