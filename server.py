"""Flask web server for the Emotion Detection application."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion_route():
    """
    Handle emotion detection requests from the web interface.
    Calls the emotion_detector function and formats the output
    exactly as required by the project instructions.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the packaged function
    result = emotion_detector(text_to_analyze)

    # Handle blank input (dominant_emotion = None)
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Format the output
    formatted = (
        f"For the given statement, the system response is "
        f"'anger' : {result['anger']}, "
        f"'disgust' : {result['disgust']}, "
        f"'fear' : {result['fear']}, "
        f"'joy' : {result['joy']} and "
        f"'sadness' : {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
