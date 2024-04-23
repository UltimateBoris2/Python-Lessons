a = int(input())
b = 0
n = []
while 2 ** b < a:
    n.append(2 ** b)
    b += 1
print(n)