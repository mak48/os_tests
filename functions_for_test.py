def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def quick_exp(val, power):
    result = pow(val, power // 2)
    result = result * result

    if power % 2 != 0:
        result = result * val
    return result
