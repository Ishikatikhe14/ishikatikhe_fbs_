#5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(words[0])):
    s = set(word[:i+1] for word in words)

    if len(s) == 1:
        prefix = words[0][:i+1]
    else:
        break

print("Longest common prefix:", prefix)