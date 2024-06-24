from flask import Flask

app = Flask(__name__)


@app.route('/notifySuccess', methods=['GET', 'POST'])
def notifySuccess():
    return "success"


@app.route('/notifyFailure', methods=['GET', 'POST'])
def notifyFailure():
    return "failure"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)