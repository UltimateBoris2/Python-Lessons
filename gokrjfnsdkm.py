def OnEtWo(a,b):
    c = 0
    if a > b:
        for i in range(b,a + 1):
            c += i
        return c    
    elif a == b:
        return a
    else:
        for i in range(a,b + 1):
            c += i
        return c

a = int(input())
b = int(input())
print ('')
print ((OnEtWo(a,b)))
print ('^^^^^^^^^^^^^^^   This is what happens if you add up all the numbers in beetween yours :) ')