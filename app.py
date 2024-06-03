import time

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    ip = request.remote_addr
    print('请求首页', ip)
    return render_template("index.html")



@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist("files")
    list = []
    for file in files:
        pdf_path = "uploads/" + str(time.time())
        file.save(pdf_path)


        info['文件名称'] = file.filename


        list.append(info)

    print(list)


    return render_template("result.html",
                           list=list,
                           cols=json.dumps(INV_KEYS, ensure_ascii=False),
                           data=json.dumps(list, ensure_ascii=False),
                           python_version=python_version
                           )



if __name__ == '__main__':
    app.run(host='0.0.0.0')
