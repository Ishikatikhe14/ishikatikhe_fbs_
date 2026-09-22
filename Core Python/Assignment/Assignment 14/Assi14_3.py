words = ["apple", "banana", "apple", "mango", "banana", "apple"]

unique = set(words)

for word in unique:
    print(word, ":", words.count(word))