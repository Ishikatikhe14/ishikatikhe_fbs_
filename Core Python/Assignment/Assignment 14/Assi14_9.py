numbers = [1, 2, 3, 4, 5, 6]
target = 9

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == target:
                print(a, b, c)