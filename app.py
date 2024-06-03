import time

from flask import Flask, render_template, request

import orc_util
import os

app = Flask(__name__)

if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route('/')
def home():
    ip = request.remote_addr
    print('请求首页', ip)
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # 确保上传文件夹存在


    pdf_path = "uploads/temp_" + str(time.time()) + "_" + file.filename
    file.save(pdf_path)
    result = orc_util.parse(pdf_path)
    os.remove(pdf_path)

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
