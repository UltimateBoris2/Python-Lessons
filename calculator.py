def calculator(FN,symbol,SN):
    answer = ''
    if symbol == '+':
        answer = FN + SN
    elif symbol == '//' or symbol == '/':
        if SN == 0:
            answer = 'you can not divide by zero stupid'
        else:
            answer = FN // SN
    elif symbol == '*':
        answer = FN * SN
    elif symbol == '-':
        answer = FN - SN
    else:
        answer = 'what is your symbol?'
    return answer
print(calculator(0,'/',100))