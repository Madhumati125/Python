def r(n):
    if n <= 1:
        return n
    else:
        return(r(n-1) + r(n-2))
n = int(input("How many terms? "))
if n <= 0:
    print("Please enter a positive integer")
else:
    for i in range(n):
        print(r(i))