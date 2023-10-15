# Time estimate: 30 minutes

text = input("Enter a string: ")

# Split the input text into words
words = text.split()

# Create a dictionary to store word counts
word_counts = {}

# Count the occurrences of each word
for word in words:
    word = word.lower()  # Convert to lowercase to make it case-insensitive
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find the length of the longest word for alignment
max_word_length = max(len(word) for word in word_counts)

# Sort the words alphabetically
sorted_words = sorted(word_counts.keys())

# Print the counts with aligned formatting
for word in sorted_words:
    count = word_counts[word]
    print(f"{word:>{max_word_length}} : {count}")
