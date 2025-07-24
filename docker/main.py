from predictable_jokes.jokes import tell_joke
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Tell a joke with optional topic and complexity.')
    parser.add_argument('--topic', type=str, default='',
                      help='The topic of the joke')
    parser.add_argument('--complexity', type=str, default='',
                      help='The complexity level of the joke')
    return parser.parse_args()

args = parse_arguments()
tell_joke(topic=args.topic, complexity=args.complexity)
