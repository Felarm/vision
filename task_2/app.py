from flask import Flask

app = Flask(__name__)


@app.route('/images', methods=['POST'])
def image_upload(request):
    path = request.;
    pass



