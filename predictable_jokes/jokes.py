import json
import random
import os

def load_jokes():
    """
    Load jokes from the jokes.json file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "jokes.json")

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def tell_joke(topic=None, complexity=None, print_joke=True, return_joke=False):
    """
    Fetch a joke, optionally filtered by topic or complexity.

    Args:
        topic (str, optional): Filter by topic.
        complexity (str, optional): Filter by complexity ('easy', 'medium', 'hard').

    Returns:
        str: A joke matching the filters, or a fallback message if none found.
    """
    jokes = load_jokes()

    # Apply filters if provided
    if topic:
        jokes = [j for j in jokes if topic in j['topics']]
    if complexity:
        jokes = [j for j in jokes if j['complexity'] == complexity]

    # If no jokes match, return a friendly message
    if not jokes:
        missing_filter = f"topic '{topic}'" if topic else f"complexity '{complexity}'"
        if topic and complexity:
            missing_filter = f"topic '{topic}' and complexity '{complexity}'"
        return f"Sorry, no jokes found for {missing_filter}. Try another search!"

    # Select a random joke from the filtered list
    joke_data = random.choice(jokes)
    joke = joke_data['joke']

    # Ensure multi-line jokes are printed correctly
    if isinstance(joke, list):
        joke = "\n".join(joke)

    if print_joke:
        print("\n" + joke + "\n")
    
    if return_joke:
        return joke
    else:
        return None