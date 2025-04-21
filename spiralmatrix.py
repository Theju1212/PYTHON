a = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 7, 9, 10, 11, 12, 13],
    [15, 16, 17, 13, 18, 23, 19],
    [23, 45, 67, 34, 25, 34, 98],
    [12, 54, 76, 89, 32, 56, 45]
]

top = 0
bt = len(a) - 1
left = 0
right = len(a[0]) - 1

while top <= bt and left <= right:
    # → Print top row
    for i in range(left, right + 1):
        print(a[top][i], end=' ')
    top += 1

    # ↓ Print right column
    for i in range(top, bt + 1):
        print(a[i][right], end=' ')
    right -= 1

    # ← Print bottom row
    if top <= bt:
        for i in range(right, left - 1, -1):
            print(a[bt][i], end=' ')
        bt -= 1

    # ↑ Print left column
    if left <= right:
        for i in range(bt, top - 1, -1):
            print(a[i][left], end=' ')
        left += 1
