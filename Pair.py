l = [8, 7, 2, 5, 3, 1]
n = len(l)
k = 10
for i in range(n):
    for j in range( i+1, n):
        if (l[i]+l[j]) == k:
            print(l[i], l[j])