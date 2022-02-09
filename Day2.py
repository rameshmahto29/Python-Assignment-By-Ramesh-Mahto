#day 2 Assignment
word = list(input("Enter a word: ").replace(" ", "").lower())
print(word)
d = {}
for i in word:
    d[i] = d.get(i, 0) + 1
print(d)
maximum = max(d.values())
print(maximum)
result = list(filter(lambda x:d[x] == maximum,d.keys()))
print(result)