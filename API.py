from flask import Flask, jsonify
from TextDetector import TextDetector

detector = TextDetector()
api = Flask(__name__)


@api.route('/', methods=['GET'])
def get_text():
    return jsonify(text=detector.detect_text())


if __name__ == '__main__':
    api.run()
