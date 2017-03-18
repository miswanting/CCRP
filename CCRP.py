# coding=utf-8
from wifi import Cell, Scheme
from flask import Flask, render_template, redirect
app = Flask(__name__)
main = {}
main['main_text'] = ''


@app.route("/")
def home():
    main['cmds'] = [
        {'href': 'cmd/scan_wifi', 'text': '扫描无线热点'},
        {'href': 'cmd/test', 'text': '测试'},
        {'href': 'cmd/test', 'text': '测试'},
        {'href': 'cmd/test', 'text': '测试'},
        {'href': 'cmd/test', 'text': '测试'}
    ]

    main['href'] = 'cmd/scan_wifi'
    main['caption'] = '扫描无线热点'
    return render_template('home.html', item=main)


@app.route("/cmd/<cmd>")
def do_cmd(cmd):
    main['main_text'] = ''
    print(cmd)
    exe_cmd(cmd)
    return redirect('/')


def exe_cmd(cmd):
    if cmd == 'scan_wifi':
        for each in Cell.all('wlan0'):
            print(each.ssid)
            main['main_text'] += each.ssid + '\n'
        print(main['main_text'])
    elif cmd == 'test':
        for each in range(0, 10):
            print(each)
            main['main_text'] += str(each) + '\n'
        print(main['main_text'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
