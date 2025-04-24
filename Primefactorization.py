#prime factorization using recursion

def prime(n):
    if n==1:
        return []
    for i in range(2,n+1):
        if n%i==0:
            return[i]+prime(n//i)
n=int(input("enter any num:"))
print(prime(n))

#prime factorization using recursion in while loop with 2 parameters
def prime(n,a):
    if(n==1):
        return
    i=2
    while(n%i !=0):
        i=i+1
    print(i,end=" ") 
    prime(n//i,a)   
n=int(input("enter any number:"))
prime(n,2)
