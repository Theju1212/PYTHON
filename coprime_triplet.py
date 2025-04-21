from math import gcd

# Ask user for input
user_input = input("Enter any num (e.g., 20 or 20m): ")

# Detect mode
if user_input.endswith('m'):
    a = int(user_input[:-1])  # max value allowed
    mode = 'max'
else:
    a = int(user_input)       # number of triplets wanted
    mode = 'count'

# Coprime check (one function only)
def coprime(x, y):
    return gcd(x, y) == 1

# Result list
res = []

# Start looping
i = 5
while True:
    for j in range(4, i):
        for k in range(3, j):
            if k*k + j*j == i*i:
                if coprime(i, j) and coprime(j, k) and coprime(i, k):
                    res.append((k, j, i))  # a triplet
                    if mode == 'count' and len(res) == a:
                        break
        if mode == 'count' and len(res) == a:
            break
    if mode == 'count' and len(res) == a:
        break
    if mode == 'max' and i >= a:
        break
    i += 1

# Print the triplets
print("Co-prime Triplets:")
for t in res:
    print(t)
