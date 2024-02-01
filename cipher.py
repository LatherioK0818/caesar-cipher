# import necessary libraries
import re
import string
import nltk
from nltk.corpus import words, names

# download necessary NLTK corpora
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

# Set of English words and names
english_words_set = set(words.words())
english_names_set = set(names.words())

# Function to encrypt text
def encrypt(phrase, shift):
    encrypted = []
    for char in phrase:
        if char.isalpha():
            shifted_char = shift_char(char, shift)
            encrypted.append(shifted_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

# Function to decrypt text
def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Helper function to shift a character
def shift_char(char, shift):
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

# Function to check if a word is in English
def is_english_word(word):
    return word.lower() in english_words_set

# Function to count English words in a text
def count_english_words(text):
    words = text.split()
    return sum(is_english_word(word.strip(string.punctuation)) for word in words)

# Function to crack the Caesar cipher
def crack(encrypted_text):
    best_shift = 0
    max_english_words = 0
    for shift in range(26):
        decrypted_attempt = decrypt(encrypted_text, shift)
        english_word_count = count_english_words(decrypted_attempt)
        if english_word_count > max_english_words:
            max_english_words = english_word_count
            best_shift = shift

    threshold_percentage = 0.5
    words_in_attempt = len(decrypted_attempt.split())
    if max_english_words / words_in_attempt >= threshold_percentage:
        return decrypt(encrypted_text, best_shift)
    else:
        return ""

# Example usage
if __name__ == "__main__":
    test_phrase = "What the hell is going on?"
    shift = 6
    encrypted = encrypt(test_phrase, shift)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt(encrypted, shift))
    cracked, used_shift = crack(encrypted)
    print("Cracked:", cracked, "using shift", used_shift)
