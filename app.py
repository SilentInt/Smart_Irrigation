from flask import Flask, render_template, request
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
    "irrigator": [1, 2, 3, 4]
}

data_send = {
    "1": {
        "amount": 20
    },
    "2": {
        "amount": 21
    },
    "3": {
        "amount": 22
    },
    "4": {
        "amount": 23
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

@app.route('/api/data', methods=['GET', 'POST'])
def data_collect():
    if request.method == 'POST':
        col = Collector()
        col.update(request.json)
        env = col.get_env()
        humid = col.get_humid()
        for k, v in env.items():
            print(k)
            print(v.get_temp())
            print(v.get_humid())
            print(v.get_light())
            print(v.get_update_time())
            print('')
        print('##########')
        for k, v in humid.items():
            print(k)
            print(v.get_humid())
            print(v.get_update_time())
            print(v.get_name())
            print('')
        return 'Submitted'


if __name__ == '__main__':
    app.run(debug=True)
