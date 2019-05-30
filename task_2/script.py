from urllib import request
import os
import imghdr  # для проверки валидности изображения
import argparse
import base64

parser = argparse.ArgumentParser(description='Lets find dir')
parser.add_argument('path', metavar='DIR', type=str,
                    help='put path to images here')
args = parser.parse_args()
DIR = args.path
# DIR = '/home/andrey/Prog/vision/task_2/send_img/' + input()
# здесь должна быть проверка директории и соответственно вывод exceptiona
URL = 'http://localhost:5000/images'
try:
    files = os.listdir(DIR)
    print(files)
except OSError as err:
    files = []
    print(err.args[1])
for item in files:
    print(type(item))
    item_path = DIR + '/' + item  # ma be propriate ddelimeter
    img_type = imghdr.what(item_path)
    if img_type is not None:
        print(imghdr.what(item_path))
        with open(item_path, 'rb') as file:
            #print(type(file))
            img = file.read()
            #encoded_img = img.encode('base64')
            encoded_img = base64.b64encode(img)
            print(type(encoded_img))
        #data = {'img': encoded_img}
        req = request.Request(url=URL, data=encoded_img, method='POST')
        req.add_header('Content-Type', 'image/{}'.format(img_type))
        resp = request.urlopen(req)
        print(resp)
        print('uploaded file:', file.name)  # если есть параметр
print('all images uploaded')

'''
инпут сделать из командной строки python script.py -DIR- -URL- 
многопоточность?
'''
