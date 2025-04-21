#3D prime number

#3d prime number :conditions 1. first check whether it is prime or not, 2.sum of digits 3. total no of digits
def is_prime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True
def sum_dig(a):
    x=sum([int (i) for i in str(a)])
    return x
def tot_dig(a):
    return len(str(a))

n=int(input("enter any num:"))
res=[]
a=1
while(len(res)!=n):
    if(is_prime(a)):
        s=sum_dig(a)#sum of digits
        tot=tot_dig(a)#total no of digits
        if(is_prime(s)) and is_prime(tot):
            res.append(a)
    a=a+1
print(res)
