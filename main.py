from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def entry():
    payload = request.get_json(force=True)

    return str(payload)

if __name__ == '__main__':
    app.run(debug=True)