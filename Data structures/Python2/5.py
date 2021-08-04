def bon(w):
    y = list()
    w = w.lower()
    for i in x:
        y.append(i)

    for i in range(1,len(y)):
        if(y[i-1] == y[i]):
            return(4*(ord(y[i])-96))



x = input("Enter secret code : ")
print(bon(x))