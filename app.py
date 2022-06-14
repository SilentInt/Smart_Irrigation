from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data', methods=['GET', 'POST'])
def dataCollect():
    if request.method == 'POST':
        print(request.form['name'])
        print(request.form['value'])
    return 'Submitted'


if __name__ == '__main__':
    app.run(debug=True)
