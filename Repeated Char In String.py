s = "itininiytnnhn"
ch = {}
for i in s:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1
print(ch)
m = max(ch, key = ch.get)
print(m)