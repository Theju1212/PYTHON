#password criteria
n=input("enter any passsword:")
dg=0
sm=0
up=0
sp=0
if(len(n)>7):
    for i in n:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            sm=sm+1
        elif(i.isdigit()):
            dg=dg+1
        elif not i.isalnum():  # not a letter or digit = special character
            sp += 1
    if(up>0 and sm>0 and dg>0 and sp>0):
        print("Good password")
    else:
        print("Bad passowrd")
else:
    print("Bad due to less number of characters")
