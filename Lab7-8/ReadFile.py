import random
from collections import Counter

# List of some sample words
words_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'pineapple', 'pear', 'peach', 'cherry']

# Create a text file and write random words to it
with open('example.txt', 'w') as file:
    for _ in range(100):  # Add 100 random words to the file
        word = random.choice(words_list)  # Choose a random word from the list
        file.write(word + ' ')  # Write the word followed by a space

# Read the content from the text file
with open('example.txt', 'r') as file:
    content = file.read()

# Split the content into words
words = content.split()

# Count the frequency of each word
word_counts = Counter(words)

# Print the word counts
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
