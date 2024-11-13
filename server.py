from flask import Flask, request, jsonify
from app.emotion_detector import emotion_predictor
from app.utils import format_emotion_output

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        emotions = emotion_predictor(text)
        formatted_emotions = format_emotion_output(emotions)
        return jsonify(formatted_emotions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)