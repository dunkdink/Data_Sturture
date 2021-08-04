import math
print("*** New Range ***")
inputs = list(map(float, input("Enter Input : ").split()))

def range():
    if(len(inputs)==1):
        i = 0.0
        print("(",end="")
        while(i<inputs[0]):
            if(inputs[0]-i<=1):
                print(i,end="")
            else:
                print(i,end=", ")
            i += 1
        print(")",end="")

    elif(len(inputs)==2):
        i = inputs[0]
        print("(",end="")
        while(i<inputs[1]):
            if(inputs[1]-i<=1):
                print(i,end="")
            else:
                print(i,end=", ")
            i += 1
        print(")",end="")

    elif(len(inputs)==3):
        i = inputs[0]
        print("(",end="")
        while(i<inputs[1]):
            if(inputs[1]-i<=inputs[2]):
                print(round(i,5),end="")
            else:
                print(round(i,5),end=", ")
            i = i +inputs[2]
        print(")",end="") 

range()