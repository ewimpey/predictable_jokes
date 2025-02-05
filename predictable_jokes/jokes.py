import json
import random
import os

def load_jokes(file_path):
    """
    Load jokes from a JSON file.
    
    Args:
        file_path (str): The path to the jokes JSON file.
    
    Returns:
        list: A list of jokes with metadata.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        jokes = json.load(file)
    return jokes

def tell_joke(topic=None, complexity=None):
    """
    Fetch a joke optionally filtered by topic or complexity.

    Args:
        topic (str, optional): Topic to filter jokes.
        complexity (str, optional): Complexity level ('easy', 'medium', 'hard').

    Returns:
        str: A joke matching the filters, or a fallback message.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data', 'jokes.json')
    jokes = load_jokes(file_path)

    # Apply filters if provided
    if topic:
        jokes = [j for j in jokes if topic in j['topics']]
    if complexity:
        jokes = [j for j in jokes if j['complexity'] == complexity]

    return random.choice(jokes)['joke'] if jokes else "No jokes found for this filter."
