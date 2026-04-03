"""This module implements the emotion detection function for the Final Project."""

import json
import requests

def emotion_detector(text_to_analyze):
    """Send text to the Watson NLP EmotionPredict API and return the raw response."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
            }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    # Convert JSON string to dictionary
    result = json.loads(response.text)

     # Handle blank input → API returns status_code 400
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
           # Extract emotion scores
    emotions = result["emotionPredictions"][0]["emotion"]

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return required output format
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
