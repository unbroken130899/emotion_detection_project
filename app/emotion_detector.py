from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
WATSON_API_KEY = os.getenv("WATSON_API_KEY")
WATSON_URL = os.getenv("WATSON_URL")

# Initialize Watson NLP API client
nlu = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=WATSON_API_KEY
)
nlu.set_service_url(WATSON_URL)

def emotion_predictor(text):
    """Analyzes emotions in the given text."""
    if not text:
        raise ValueError("Input text cannot be empty")
    
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    
    # Extract emotions from response
    emotions = response['emotion']['document']['emotion']
    return emotions