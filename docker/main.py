from predictable_jokes.jokes import tell_joke
import os

def get_topic():
    if os.getenv("TOPIC"):
        return os.getenv("TOPIC")
    else:
        return "data science"
    
def get_complexity():
    if os.getenv("COMPLEXITY"):
        return os.getenv("COMPLEXITY")
    else:
        return "medium"

tell_joke(topic=get_topic(), complexity=get_complexity())
