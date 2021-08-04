def toend(n):
    if n==num:
        print("".join(x))
        return
    x[n]="0"
    toend(n+1)
    x[n]="1"
    toend(n+1)

num=int(input("Enter Number : "))
x=["0"]*num
if num<0:
    print("Only Positive & Zero Number ! ! !")
elif num==0:
    print("0")
else:
    toend(0)