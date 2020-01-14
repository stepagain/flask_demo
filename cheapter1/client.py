from flask import Flask, render_template, Response,jsonify,request
import json
import requests
app = Flask(__name__)
app.app_context()

url = 'http://127.0.0.1:8006'

def up_img():
    img_path = 'E:/ZYG_WORK/Pixel-Anchor/data/train/train_img/img_2.jpg'
    files  = {'image': open(img_path,mode='rb')}
    r = requests.post(url + '/upload',files=files)
    resJson = json.loads(r.text)
    return json.dumps(resJson)

def post_json():
    data = {'imgUrl': 'path.jpg', 'id': 0}
    json_data = json.dumps(data)
    user_info = {'info': 'Lenna'}
    r = requests.post(url + '/upload_json', data=json_data)
    # r = requests.post(url + '/upload_json', data=json_data,file = files)
    resJson =  json.loads(r.text)
    return resJson



if __name__ == '__main__':
    # app.run(debug = True)
    # up_img()
    post_json()