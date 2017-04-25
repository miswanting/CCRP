# coding=utf-8
import time
import random
import hashlib
from wifi import Cell, Scheme
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
currentPage = 'index.html'
main = {}
main['main_text'] = []


@app.route("/")
def home():
    main['cmds'] = [
        {'href': 'cmd/scan_wifi', 'text': '扫描无线热点'},
        {'href': 'cmd/test', 'text': '测试'},
        {'href': 'd3', 'text': 'D3测试'},
        {'href': 'cmd/test', 'text': '测试'},
        {'href': 'cmd/test', 'text': '测试'}
    ]

    main['href'] = 'cmd/scan_wifi'
    main['caption'] = '扫描无线热点'
    with app.test_request_context():
        main['css_file'] = url_for(
            'static', filename='style.css', q=get_hash())
    return render_template(currentPage, item=main)


@app.route("/d3")
def d3():
    with app.test_request_context():
        main['js_file'] = url_for(
            'static', filename='d3_test.js', q=get_hash())
    return render_template('d3.html', item=main)


@app.route("/cmd/<cmd>")
def do_cmd(cmd):
    main['main_text'] = []
    print(cmd)
    exe_cmd(cmd)
    return redirect('/')


def exe_cmd(cmd):
    cmd = cmd.split('+')
    if cmd[0] == 'scan_wifi':
        for each in Cell.all('wlan0'):
            main['main_text'].append(
                {'href': 'cmd/connect+' + each.ssid, 'text': each.ssid})
    elif cmd[0] == 'test':
        for each in range(0, 10):
            main['main_text'].append({'href': each, 'text': each})
    elif cmd[0] == 'connect':
        print(cmd[1])


def get_hash():
    m = hashlib.md5()
    m.update(str(time.time()).encode("utf-8"))
    m.update(str(random.random()).encode("utf-8"))
    return m.hexdigest()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
