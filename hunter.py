from collections import Counter

l = ['a', 'a', 'a', 'a', 'b']

s = Counter(l)

print(s)

print(s.most_common(1)[0][0])

