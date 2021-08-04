x = input("Enter String and Code : ").split(",")

textlist = list()

for i in x[0]:
    if(i != " "):
        textlist.append(i)

numlist = list()
newtext = list()
for i in x[1]:
    numlist.append(int(i))


for i in range(len(textlist)):
    if(ord(textlist[i]) < 91):
        temp = ord(textlist[i]) + (numlist[i % len(numlist)])
        if(temp > 90):
            temp=temp - 26


    if(ord(textlist[i]) > 96):
        temp=ord(textlist[i]) + (numlist[i % len(numlist)])
        if(temp > 122):
            temp=temp - 26
    newtext.append(chr(temp))

print("Encode message is : ",newtext)
print("Decode message is : ",textlist)

