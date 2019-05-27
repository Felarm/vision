import requests
import os
import imghdr  # для проверки валидности изображения
import argparse

parser = argparse.ArgumentParser(description='Lets find dir')
parser.add_argument('path', metavar='DIR', type=str,
                    help='put path to images here')
parser.add_argument('url', metavar='URL', type=str,
                    help='put url to upload')
args = parser.parse_args()
print(args.path, args.url)
DIR = args.path
URL = args.url
# DIR = '/home/andrey/Prog/vision/task_2/send_img/' + input()
# здесь должна быть проверка директории и соответственно вывод exceptiona
# URL = 'http://localhost:5000/image'

for item in os.listdir(DIR):
    if imghdr.what(DIR + item) is not None:
        print(imghdr.what(DIR + item))
        with open(DIR + item, 'rb') as file:
            files = {'img': file}
            r = requests.post(URL, files=files)
            print(r)
            print('uploaded file:', file.name)  # если есть параметр
print('all images uploaded')

'''
инпут сделать из командной строки python script.py -DIR- -URL- 
многопоточность?
'''
