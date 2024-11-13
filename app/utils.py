def format_emotion_output(emotions):
    """Formats emotion data with percentages rounded to two decimals."""
    return {emotion: f"{score:.2f}" for emotion, score in emotions.items()}