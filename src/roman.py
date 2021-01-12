def roman(num):
    numbers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    i = 0
    while  num > 0:
        for _ in range(num // numbers[i]):
            result += symbols[i]
            num -= numbers[i]
        i += 1
    return result