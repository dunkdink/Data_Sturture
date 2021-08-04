x = input("Enter people and time : ").split(" ")

mainline = list()
time = int(x[1])
cashier1 = list()
cashier2 = list()


for i in x[0]:
    mainline.append(i)

c2 = 0

for j in range(time):
    print(j+1, end=" ")

    if(len(cashier2) > 0):
        c2 += 1
    
    if(c2 % 2 == 0 and len(cashier2) != 0):
        cashier2.pop(0)
        c2=0    
    
    if(j % 3 == 0 and len(cashier1) != 0):
        cashier1.pop(0)

    if(len(mainline) != 0):
        if(len(cashier1) < 5):
            cashier1.append(mainline.pop(0))

        else:
            cashier2.append(mainline.pop(0))



    print(mainline, cashier1, cashier2)
