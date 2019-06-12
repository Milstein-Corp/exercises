from collections import defaultdict

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

def supa():
    return []

citis_by_state = defaultdict(lambda: [])


for c in city_list:
    citis_by_state[c[0]].append(c[1])

for s, c in citis_by_state.items():
    print("state: % s -> cities: %s " % (s, c))




# a = {"a": 0, "b":1, "c":2}
# print(a)
# print(type(a))
# print(len(a))
# print(a.keys())
# print(type(a.keys()))
# for k in a.keys():
#     print(k)
#     print(a[k])
#     print(a.get(k))
#
# print(a["a"])
# print(a["i"])
# print(a.get("i"))

# Does my dict have a "y" as a key?

# print(a.get("y"))
#
# print(a.values())
#
# for v in a.values():
#     print(v)
#
# l = list(a.keys())
# print(l)
# print(type(l))
#
# for k,v in a.items():
#     print("key: %s -> value: %s" %(k, v))
#
# tuples = list(a.items())
# print(tuples)

# a = collections.defaultdict(lambda: "i")
# b = dict()
#
#
# a["a"] = "greenlight"
# a["b"]
#
# b["a"] = "shoot"
# b["b"] = "regular"
#
# print(a)
# print(b)
#
# for k in a.values():
#     print(k)
#
# for k in b.values():
#     print(k)






