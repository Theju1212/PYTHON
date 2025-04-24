def abc(a):
    if a==4:
        return
    a+=1
    abc(a)
    print("cse",end='')
    abc(a)
    print("mech",end='')

def main():
    num="12"
    for i in num:
        print()
        abc(int (a))
main()

def abc(n):
    if n==1:
        return 2
    b=abc(n-1)
    print("hai",end='')
    return b+1
print(abc(5))
