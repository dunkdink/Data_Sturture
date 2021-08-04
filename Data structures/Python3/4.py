class StackCalc:

     def __init__(self):
         self.lst = []
         self.valid = ["DUP","+","-","/","*","POP","PSH"]
         self.order = ["+","-","/","*"]
         self.operand = [lambda x: x[0] + x[1],lambda x: x[0] - x[1],lambda x: x[0] / x[1],lambda x: x[0] * x[1]]
         self.value = 0
         self.Invalid = False

     def run(self,arg):
         self.value = 0
         for i in arg.split():
             if ( not self.isNumber(i) and i not in self.valid):
                 print("Invalid instruction:",i)
                 self.Invalid = True
                 break
             else:
                 if(self.isNumber(i)):
                     self.lst.append(i)
                 else:
                     if(i == "DUP"):
                         t = self.lst[-1:][0]
                         self.lst.append(t)
                     elif(i == "POP"):
                         self.lst.pop()
                     elif(i == "PSH"):
                         pass
                     else:
                         if(len(self.lst) > 1):
                             l = [int(self.lst.pop()),int(self.lst.pop())]
                             self.lst.append(int(self.operand[self.order.index(i)](l)))
                    
     def getValue(self):
         if(not self.Invalid):
             return  self.lst[-1:][0] if len(self.lst) > 0  else 0
         else:
             return ''
    
     def isNumber(self,x):
         try:
             int(x)
             return True
         except ValueError:
             return False


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
