from flask import Flask, render_template, Response,jsonify,request
from datetime import  datetime
import json
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# https://www.letianbiji.com/python-flask/py-flask-upload-file.html


def secure_filename(filename):
    ext =  filename.rsplit('.', 1)[-1]
    now_dt =   datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3]
    return '{0}.{1}'.format(now_dt,ext)



# Determine if the file name is in a format we support
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



@app.route('/upload', methods=["POST"])
def upload():
    upload_files = request.files['image']
    ## get file's content
    # file_content = request.files['image'].stream.read()
    if upload_files and allowed_file(upload_files.filename):
        filename = secure_filename(upload_files.filename)
        upload_files.save(os.path.join(app.root_path,app.config['UPLOAD_FOLDER'],filename))
        return {'status': 200}
    else:
        return json.dumps({'status':'failed'})


#
@app.route("/upload_json", methods=["POST"])
def upload_json():
    json_data = request.get_data()
    data = json.loads(json_data)
    print(data)
    if data:
        url = data["imgUrl"]
        task_id = data["id"]
        return {'status': 200}
    else:
        return json.dumps({'status': 'failed'})

if __name__=='__main__':
    app.run(host='127.0.0.1',
            port='8006',
            debug=True)