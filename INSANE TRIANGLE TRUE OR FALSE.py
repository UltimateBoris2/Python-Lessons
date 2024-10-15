def triangle_checker(FA,SA):
    if FA + SA >= 180:
        return 'ERROR'
    elif FA <= 0 or SA <= 0:
        return 'ERROR'
    else:
        return 180 - (FA + SA)
print(triangle_checker(90,90))