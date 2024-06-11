def STH(a):
    if a <= -2:
        return 1 - (a + 2)**2
    elif a > -2 and a <= 2:
        return -(a / 2)
    else:
        return (a - 2) **2 + 1
a = float(input())
print(STH(a))