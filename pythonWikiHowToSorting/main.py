import re

print("90A80B".isalnum())
print("1111223".isdigit())
print("ddaaddd".strip("d"))
print("0h11101".isdecimal())
print("yyy".center(5, "9"))
print("asdf".count("a", 1))
print("aaaaddaaad".find("dd",0,10))
a = "aaaaddaaaad"
ind = a.find("dd")
print(a[ind:ind+len("dd")])
print(a.find("aaaaaaaaaaaa",0,10))



print("88aabaa88".strip(r'\d'))

string="asdf999"


result = re.sub(f"\d+", "", string)
print(result)


y = "aaa8888aaa888"
print("".join([i for i in y if i.isdigit()]))
print("".join([i for i in y if i.isalpha()]))
