from flask import Flask, jsonify, request
from flask_classful import FlaskView, route
from TextDetector import TextDetector


class APIView(FlaskView):

    def __init__(self):
        self.text = 'Text in image have not been detected yet'
        self.detector = TextDetector()

    @route('/', methods=['GET', 'POST'])
    def handle_text(self):
        if request.method == 'POST':
            self.text = self.detector.detect_text()
        return jsonify({"text": self.text})


if __name__ == '__main__':
    app = Flask(__name__)
    APIView.register(app)
    app.run()
