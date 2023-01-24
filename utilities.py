import random
from auth import *

def getRandomFile():

    drive = getGoogleAuth()

    print("GETTING A FILE")

    file_list = drive.ListFile().GetList()

    file = random.choice(file_list)

    title = file['title']
    extension = title.split(".")[1]

    # downloads file, which is deleted later
    file.GetContentFile(title)

    return {'title': title, 'extension': extension}