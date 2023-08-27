from flask import Flask, request, jsonify
from flask_cors import CORS
import datascraper

app = Flask(__name__)
CORS(app)


@app.route('/data', methods=['GET'])
def recommend_movies():
    res = datascraper.getData(request.args.get('index'))
    return jsonify(res)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
