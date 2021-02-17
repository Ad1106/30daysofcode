T=int(input())
for i in range(T):
    str=input()
    res=list(str)
    l=len(res)
    p=0
    if(l%2==1):
        for k in range (l//2+1):
            print(res[p],end="")
            p+=2
        p=1
        print(end=" ")
        for k in range (l//2+1,l):
            print(res[p],end="")
            p+=2
        print("")
    elif(l%2==0):
        for k in range (l//2):
            print(res[p],end="")
            p+=2
        p=1
        print(end=" ")
        for k in range (l//2,l):
            print(res[p],end="")
            p+=2
        print("")
