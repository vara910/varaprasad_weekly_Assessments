sentence = input("Enter a sentence: ")

def word_count(sentence):
    words = sentence.lower().split()  # Convert to lowercase and split into words
    word_freq = {}  

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1  # Count occurrences

    return word_freq
count = word_count(sentence)
print("\nWord Count:")
for word, count in count.items():
    print(f"{word}: {count}")
