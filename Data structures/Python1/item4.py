'''สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)

def num_grid(lst):

    #Code Here

    return lst



'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []

input_list = input().split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n") '''




print("*** Minesweeper ***")
def num_grid(lst):
  for i in range(0,5):
    for j in range(0,5):
      if lst[i][j]=='-':
        num  = 0
        if i!=0:
          if lst[i-1][j]=='#':
            num+=1
        if i!=4:
          if lst[i+1][j]=='#':
            num+=1
        if  j!=0 and i!=0:
          if lst[i-1][j-1]=='#':
            num+=1
        if  j!=0:
          if lst[i][j-1]=='#':
            num+=1
        if  j!=0 and i!=4:
         if lst[i+1][j-1]=='#':
            num+=1
        if j!=4 and i!=0:
          if lst[i-1][j+1]=='#':
            num+=1
        if j!=4:
          if lst[i][j+1]=='#':
            num+=1
        if j!=4 and i!=4:
          if lst[i+1][j+1]=='#':
            num+=1
       
        lst[i][j] = str(num)
  return lst



'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []

input_list = input("Enter input(5x5) : " ).split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")