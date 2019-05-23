import requests
import os

DIR = '/home/andrey/Prog/vision/task_2/send_img/' + input()
URL = 'http://localhost:5000/images'

for item in os.listdir(DIR):
    if '.png' in item:
        files = {'img': open(DIR+item, 'rb')}
        r = requests.post(URL, files=files)
print(r)
