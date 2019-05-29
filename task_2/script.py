from urllib import request, parse
import base64
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
try:
    files = os.listdir(DIR)
except OSError as err:
    files = []
    print(err.args[1])
for item in files:
    item_path = DIR + '\\' + item
    img_type = imghdr.what(item_path)
    if img_type is not None:
        print(imghdr.what(item_path))
        with open(item_path, 'rb') as file:
            encoded_img = base64.b64encode(file.read())
            print(type(file))
        print(type(encoded_img))
        req = request.Request(url=URL)
        req.add_header('Content-type', 'image/{}'.format(img_type))
        resp = request.urlopen(req, data=encoded_img)
        print(resp.info)
        print('uploaded file:', file.name)  # если есть параметр
print('all images uploaded')

'''
инпут сделать из командной строки python script.py -DIR- -URL- 
многопоточность?
'''
