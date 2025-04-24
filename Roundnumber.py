#round number
#conditions: 1. first starting with any poasitive num, replace  the num by the sum of the squares of its digits
#2.repeat the process until the process is equal to 1
def isround(n):
    res=[]
    while(n!= 1):
        
        if(n in res):
            return False
        res.append(n)
        n=sum(int(i)*int(i) for i in str(n))
    return True
print(isround(19))
print(isround(10))
print(isround(34))