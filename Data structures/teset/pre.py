'''
print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split()
if int(h)<0:
    print(f"hh({h}) is invalid!")
if int(m)<0 or int(m)>=60:
    print(f"mm({m}) is invalid!")
if int(s)<0 or int(s)>=60:
    print(f"ss({s} is invalid!)")

sec = int(s)
sec += int(m)*60
sec+=int(h)*3600

if len(h)==1:
    h='0'+h
if len(m)==1:
    m='0'+m
if len(s)==1:
    s='0'+s

print(f"{h}:{m}:{s} =",format(sec,',d')," seconds")
'''

'''print("*** Converting hh.mm.ss to seconds ***")
x,y=map(int,input("Enter num1 num2 : "))
if x*y<1000:
    sum=x*y
    print(sum)
else:
    sum=x+y
    print(sum)
'''

'''def Rshift(num,shift):
    n=num
    s=shift
    result=n>>s
    return(result)

n,s=input("num").split()
print(Rshift(int(n),int(s)))
'''
'''
print("*** Wind classification ***")
x=int(input("Enter wind speed (km/h) : "))
if x<0:
    print("!!!Wrong value can't classify.")
else:
    if x<52:
        ans='Breeze'
    elif x<56:
        ans='Depression'
    elif x<102:
        ans='Tropical Storm'
    elif x<209:
        ans='Typhoon'
    elif x>209:
        ans='Super Tyhoon'
    print(f"Wind classification is {ans}")
'''
'''
print(" *** class MyInt ***")
x,y=map(int,input("Enter 2 number : ")):
def isPrime(num):
    counter=0
    for i in range(1,num+1):
        if num%i ==0:
            counter+=1
    if counter>2 or counter==1:
        return False
    else:
        return True

print(f"{x} isPrime :",isPrime(x))
print(f"{y} isPrime :",isPrime(y))

print(f"Prime number between 2 and {x} : ")
for i in range(1,x+1):
    if isPrime(i):
        print(i,end="")
print("")
print(f"Prime number between 2 and {y} : ")
for i in range(1,y+1):
    if isPrime(i):
        print(i,end="")
'''