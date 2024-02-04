
from collections import Counter
import re


def most_frequent_word_length(string):
    """
    This function takes a string as input, and counts the frequency of each word in the string,
    there might  be repeated characters in the string. Your task is to find the highest frequency
    and returns the length of the  highest-frequency word.
    Args:
        string: The input string.
    Returns:
        The length of the highest-frequency word.
    """
    # Split the string into words, removing punctuation and converting to lowercase.
    words = re.findall(r'\b\w+\b', string.lower())
    # Count the word frequencies using Counter.
    word_counts = Counter(words)
    # Find the word with the highest frequency.
    max_length_word = max(word_counts, key=word_counts.get)
    # Return the length of the highest-frequency word.
    return len(max_length_word)

# Test cases
string1 = "write write write all the number from from from 1 to 100"
string2 = "hello world hello world this is a test"
string3 = "the quick brown fox jumps over the lazy dog"

print(most_frequent_word_length(string1))  # Output: 5
print(most_frequent_word_length(string2))  # Output: 5
print(most_frequent_word_length(string3))  # Output: 3

