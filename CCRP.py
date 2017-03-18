# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    a = {}
    a['href'] = 'CCRP.py'
    a['caption'] = '扫描无线热点'
    return render_template('home.html', item=a)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
