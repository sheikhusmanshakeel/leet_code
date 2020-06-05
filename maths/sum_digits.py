def sumDigits(n):
    sum = 0
    count = 0
    while n > 0:
        count += 1
        sum += n % 10
        n //= 10
    print("loop count: {0}".format(count))
    return sum


data1 = 123
target1 = 6
assert sumDigits(data1) == target1


data2 = 123456123456
target2 = 42
assert sumDigits(data2) == target2