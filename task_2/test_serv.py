from flask import Flask
from flask import request
from flask import json
import time
import base64
import random

app = Flask(__name__)


@app.route('/images', methods=['POST'])
def image_upload():
    #x = request.data['img'].decode()
    x = base64.b64decode(request.get_data())
    ext = request.content_type
    print(type(x))  # base64.decodestring(request.get_data())
    #img = open('test.jpg', 'xb')
    img = open('test{}.{}'.format(random.randrange(1, 199), ext[-3:]), 'xb')
    img.write(x)
    img.close()
    print(type(x))
    print(request.headers)
    return 'Success'
