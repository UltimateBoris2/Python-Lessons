def triangle_real_or_fake(FN,SN,TN):
    helper = 0
    if FN + SN > TN:
        helper += 1
        if TN + FN > SN:
            helper += 1
            if SN + TN > FN:
                helper += 1
    else:
        return 'so fake'
    if helper == 3:
        return 'real'
    else:
        return 'so fake'


print(triangle_real_or_fake(12,10,8))