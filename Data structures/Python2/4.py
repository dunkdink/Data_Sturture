
        

def hbd(age):
    Numerator = age%2
    Ans=age//2
    return f"saimai is just 2{Numerator}, in base {Ans}!" 

year = input("Enter year : ")

print(hbd(int(year)))
 