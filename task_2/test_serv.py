from flask import Flask
from flask import request
from flask import json
import time

app = Flask(__name__)


@app.route('/images', methods=['POST'])
def image_upload():
    x = request.files['img'].save(dst='test'+str(time.time())+'.jpg')
    print(x)
    return 'Success'
