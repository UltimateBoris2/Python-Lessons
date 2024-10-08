def age_checker(age):
    if age == 77:
        return 'cool'
    elif age >= 12 and age < 100:
        return 'OK'
    elif age > 100:
        return 'stop lying about your age bruuuuuh'
    else:
        return 'wrong age'
print(age_checker(77))
