def Rshift(num,shift):
    n = num 
    s = shift
    result= n>>s  
    return(result)


n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))