a = []
while True:
    b = int(input())
    if b == 0:
        break
    a.append(b)

print (a.count(max(a)))
print ('This is how much of the biggest numbers repeated while you were trying to find zero:) ')
