import json
import requests


class SentimentAnalysisAPI:
    def __init__(self, api_key):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.sentiment_url = "https://api.edenai.run/v2/text/sentiment_analysis"
        self.ner_url = "https://api.edenai.run/v2/text/named_entity_recognition"
        self.emotion_url = "https://api.edenai.run/v2/text/emotion_detection"

    def analyze_sentiment(self, text, providers="google,amazon", language="en", fallback_providers=""):
        cleaned_text = text.replace("\n", " ").replace("\r", "")
        payload = {
            "providers": providers,
            "language": language,
            "text": cleaned_text,
            "fallback_providers": fallback_providers
        }

        return self._make_api_request(self.sentiment_url, payload)

    def analyze_ner(self, text, providers="google,amazon", language="en", fallback_providers=""):
        cleaned_text = text.replace("\n", " ").replace("\r", "")
        payload = {
            "providers": providers,
            "language": language,
            "text": cleaned_text,
            "fallback_providers": fallback_providers
        }

        return self._make_api_request(self.ner_url, payload)

    def analyze_emotion(self, text, providers="nlpcloud,vernai", fallback_providers=""):
        cleaned_text = text.replace("\n", " ").replace("\r", "")
        payload = {
            "providers": providers,

            "text": cleaned_text,
            "fallback_providers": fallback_providers
        }

        return self._make_api_request(self.emotion_url, payload)

    def _make_api_request(self, url, payload):
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            result = json.loads(response.text)
            return result
        except requests.exceptions.RequestException as e:
            return {"error": f"Error during analysis: {str(e)}"}
