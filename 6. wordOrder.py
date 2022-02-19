# You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the
# input order of appearance of the word. See the sample input/output for clarification.
# Note: Each input line ends with a "\n" character.
n = int(input())
l = {}
for i in range(n):
    k = input()
    if k in l:
        l[k] += 1
    else:
        l[k] = 1
print(len(l))
for i in l:
    print(l[i], end=" ")
