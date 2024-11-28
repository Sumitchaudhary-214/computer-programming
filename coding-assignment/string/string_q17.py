#Find the Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
print(longest_word("Find the longest word in this sentence"))  # Output: "sentence"
