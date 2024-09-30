# Sort A Dictionary
d = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
dic = sorted(d.keys())
d2 = {}
for i in dic:
    d2[i] = d[i]
print(d2)

# Sort A Dictionary (BY VALUE)
dicti = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
dict2 = {key:value for key, value in sorted(dicti.items(), key=lambda x: x[1])}
print(dict2)