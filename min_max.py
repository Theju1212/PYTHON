#max and min in the largest smallest no in the digits and print them
def biggest_digit(n):
    return max([int(i) for i in str(n)])

def smallest_digit(n):
    return min([int(i) for i in str(n)])

A = 1234
B = 3454
C = 7976

bigA = biggest_digit(A)
bigB = biggest_digit(B)
bigC = biggest_digit(C)

smallA = smallest_digit(A)
smallB = smallest_digit(B)
smallC = smallest_digit(C)

a1 = bigA + bigB + bigC
a2 = smallA + smallB + smallC

print("Sum of largest and smallest digits:", a1 + a2)
