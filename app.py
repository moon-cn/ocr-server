import sys
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
    import platform

    # 获取操作系统名称
    os_name = platform.system()
    # 获取操作系统版本
    os_version = platform.version()
    # 获取操作系统位数
    os_arch = platform.architecture()[0]

    print(f"版本: {os_version}")
    print(f"位数: {os_arch}")
    info = {
        "操作系统": os_name + " " + os_version + " " + os_arch,
        "Python 版本": sys.version,
        "ip": ip,

    }
    return render_template("index.html", info=info)


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
