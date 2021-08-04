def swap1(x):  
    c1=x[-2]+x[-1]
    c2=""
    for i in range(0,len(x)-2):
        c2+=x[i]
    return c1+c2

def swap2(x):  
    c1=x[-3]+x[-2]+x[-1]
    c2=""
    for i in range(0,len(x)-3):
        c2+=x[i]
    return c1+c2



print("*** String Rotation ***")
x,y=input("Enter 2 strings : ").split(" ")
x1=x
y1=y
counter=1
while not(x1==x and y1==y) or counter == 1:
    if counter<6:
        print(f'{counter}.{swap1(x1)} {swap2(y1)}')
    if x==swap1(x1) and y==swap2(y1) and counter>5:
        print(".............")
        print(f'{counter}.{swap1(x1)} {swap2(y1)}')

    x1=swap1(x1)
    y1=swap2(y1)
    counter+=1
print(f'total={counter-1}')