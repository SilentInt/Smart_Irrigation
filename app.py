from flask import Flask, render_template, request, jsonify

import EnvSensor
import HumidSensor
from Collector import Collector

app = Flask(__name__)
app.config.update(DEBUG=True)

data_recv = {
    "mac": "ff:ff:ff:ff:ff:11",
    "env": {
        "temp": 22.4,
        "humid": 32.5,
        "light": 70.3
    },
    "sensors": {
        "11:11:11:11:11:11": {
            "humid": 21.1
        },
        "11:11:11:11:11:12": {
            "humid": 22.2
        },
        "11:11:11:11:11:13": {
            "humid": 23.3
        }
    },
    "irrigator": 3
}

data_send = [
    {
        "port": '1',
        "amount": 100
    }
]
request_json = {"mac": "ff:ff:ff:ff:ff:11"}

bind = {
    "11:11:11:11:11:11": {
        'mac': "fsdfasdf",
        'port': 3
    }
}


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/api/data', methods=['GET', 'POST'])
# def data_collect():
#     if request.method == 'POST':
#         print(request.form['name'])
#         print(request.form['value'])
#     return 'Submitted'

@app.route('/api/data', methods=['POST'])
def data_collect():
    if request.method == 'POST':
        col = Collector()
        col.update(request.json)
        irrigators = col.irrigators
        for irr_obj in irrigators.values():
            col.add_task(irr_obj)
        return 'Submitted'


@app.route('/api/task', methods=['POST'])
def get_task():
    col = Collector()
    print('Receive task request from', request.json['mac'])
    tasks = col.get_task(request.json['mac'])
    print("data to response", tasks)
    return jsonify(tasks)


@app.route('/api/bind', methods=["POST"])
def bind_sensors():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
