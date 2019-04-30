minlen = len(leafs[0])
for leaf in leafs:
    if (len(leaf) < minlen):
        minlen = len(leaf)

newleafs = []
for leaf in leafs:
    if (len(leaf) == minlen):
        newleafs.append(leaf)

numleafs = []
for leaf in newleafs:
    numleafs.append(int(leaf[::-1]))

print(numleafs)

min = numleafs[0]
for leaf in numleafs:
    if (leaf < min):
        min = leaf

min = str(min)
min = min[::-1]

result = ''

alp = {'0': 'a', '1': 'b'}

for c in min:
    print(alp.get(c))
    result = alp.get(c) + result

print(result)