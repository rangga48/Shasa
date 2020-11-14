from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return jsonify({"response": "Get Request Called"})
    elif request.method == 'POST':
        req_Json = request.json
        name = req_Json['name']
        umur = req_Json['umur']
        nickname = req_Json['nickname']
        return jsonify({"response": "Yow" + name+" " + umur + nickname})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
