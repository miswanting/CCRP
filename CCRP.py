# coding=utf-8
from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/")
def home():
    a = {}
    a['href'] = 'cmd/scan_wifi'
    a['caption'] = '扫描无线热点'
    return render_template('home.html', item=a)


@app.route("/cmd/<cmd>")
def do_cmd(cmd):
    print(cmd)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
