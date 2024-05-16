def read_file_content(filename):
    """Reads and returns the content of a file."""
    with open(filename, 'r') as file:
        return file.read()

def count_word_frequencies(text):
    """Counts the frequency of each word in the given text."""
    words = text.split()  # Breaks down each word in a piece of text and adds it to a list called words
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies  # Adds the word to the frequencies dictionary and increments it (if it's the first time being seen, 0 is the default). If the word already exists, the count simply increments.

def print_histogram(word_frequencies):
    """Prints a text-based histogram of word frequencies."""
    for word, frequency in sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True): # The sorted function sorts the dictionary in descending order. When applying the key as Lamda the sorting is done on the values of the dictionary rather than the words (the key of the dictionary). Making reverse true sorts in desc
        print(f"{word}: {'*' * frequency}") # Each word is printed and the frequency is multipled by the astrick string therefore print it the number of times of frequency

if __name__ == "__main__":
    filename = "words.txt"
    text = read_file_content(filename)
    word_frequencies = count_word_frequencies(text.lower())  # Convert text to lower case for case-insensitive counting
    print_histogram(word_frequencies)
