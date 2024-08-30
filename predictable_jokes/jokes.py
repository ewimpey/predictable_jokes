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

def get_random_joke():
    """
    Load jokes and return a random joke.
    
    Returns:
        str: A random joke.
    """
    # Define the path to the jokes.json file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'jokes.json')
    
    # Load jokes from the file
    jokes = load_jokes(file_path)
    
    # Return a random joke from the list
    return random.choice(jokes)['joke']

def get_joke_by_topic(topic):
    """
    Return a random joke filtered by a specific topic.
    
    Args:
        topic (str): The topic to filter jokes by.
    
    Returns:
        str: A random joke from the specified topic, or a message if no jokes found.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'jokes.json')
    jokes = load_jokes(file_path)
    
    filtered_jokes = [joke['joke'] for joke in jokes if topic in joke['topics']]
    if filtered_jokes:
        return random.choice(filtered_jokes)
    else:
        return "No jokes found for this topic."

def get_joke_by_complexity(complexity):
    """
    Return a random joke filtered by a specific complexity level.
    
    Args:
        complexity (str): The complexity level to filter jokes by ('easy', 'medium', 'hard').
    
    Returns:
        str: A random joke from the specified complexity level, or a message if no jokes found.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'jokes.json')
    jokes = load_jokes(file_path)
    
    filtered_jokes = [joke['joke'] for joke in jokes if joke['complexity'] == complexity]
    if filtered_jokes:
        return random.choice(filtered_jokes)
    else:
        return "No jokes found for this complexity level."

if __name__ == "__main__":
    # Print a random joke
    print(get_random_joke())

    # Example: Print a joke filtered by topic
    print(get_joke_by_topic('machine learning'))

    # Example: Print a joke filtered by complexity
    print(get_joke_by_complexity('easy'))
