print(" *** class MyInt ***")
x,y = map(int,input("Enter 2 number : ").split())
def isPrime(num):
    counter=0
    for i in range(1,num+1):
        if num%i == 0:
            counter+=1
    if counter>2 or counter==1:
        return False
    else:
        return True
print(f"{x} isPrime :",isPrime(x))
print(f"{y} isPrime :",isPrime(y))

print(f"Prime number between 2 and {x}: ",end="")
for i in range(1,x+1):
    if isPrime(i):
        print(i,end=" ")
print("")
print(f"Prime number between 2 and {y}: ",end="")
for i in range(1,y+1):
    if isPrime(i):
        print(i,end=" ")
