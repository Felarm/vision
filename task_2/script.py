from urllib import request, error
import os
import imghdr
import argparse
import base64

parser = argparse.ArgumentParser(description='Lets find dir')
parser.add_argument('path', metavar='DIR', type=str,
                    help='put path to images here')
args = parser.parse_args()
DIR = args.path
URL = 'http://localhost:5000/images'


def upload_image(dir_path, url):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        for item in files:
            item_path = os.path.join(os.path.abspath(DIR), item)
            img_type = imghdr.what(item_path)  # проверяет валидность изображения по первым двум байтам
            if img_type is not None:
                with open(item_path, 'rb') as file:
                    img = file.read()
                    encoded_img = base64.b64encode(img)  # кодирует изображения в base64
                req = request.Request(url=url, data=encoded_img, method='POST')
                req.add_header('Content-Type', 'image/{}'.format(img_type))
                try:
                    resp = request.urlopen(req)
                    if resp.status == 200:
                        print('uploaded file:', file.name)
                except error.URLError as err:
                    print(err.reason)
        return 'all images uploaded'
    else:
        print("not a dir or dir doesn't exists")
        return


upload_image(DIR, URL)
