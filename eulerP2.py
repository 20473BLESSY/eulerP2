'''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ^1000?'''

def power(n):
    return 2** n
print(power(15))

def power_digit_sum(num):
    sum = 0
    dig = str(power(num))
    for i in dig:
        sum += int(i)
    return sum
print(power_digit_sum(1000))