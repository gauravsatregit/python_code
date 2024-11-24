def prime():
    for i in range(2,n+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i,end=" ")
    return n
n=int(input("Enter a number : "))
prime()
