class Stack:
    def __init__(self):
        self.myStack = list()
        self.unmatch = False
        self.close = False
        self.open = False

    def push(self, value):
        if(value == "(" or value == "[" or value == "{" or value == ")" or value == "]" or value == "}"):
            if(value == ")" or value == "]" or value == "}"):
                if(self.isEmpty()):
                    self.close = True
                else:
                    temp = self.pop()
                    if(value == ")"):
                        
                        if(temp != "("):
                            #print(temp, value)
                            self.unmatch = True
                    if(value == "]"):
                        if(temp != "["):
                            #print(temp, value)
                            self.unmatch = True
                    if(value == "}"):
                        if(temp != "{"):
                            #print(temp, value)
                            self.unmatch = True
            else:
                self.myStack.append(value)
            if(self.isEmpty() is False):
                self.open = True
            else:
                self.open = False
                    

    def pop(self):
        return self.myStack.pop()

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def size(self):
        return len(self.myStack)

    def getValue(self):
        value = ""
        for i in range(self.size()):
            value = value + self.pop()
        return value


x = input("Enter expresion : ")
mystack = Stack()
for i in x:
    mystack.push(i)
#print(mystack.myStack)
#print("Unmatch" , mystack.unmatch)
#print("Close" , mystack.close)
#print("Open" , mystack.open)

if(mystack.unmatch or mystack.unmatch and mystack.close):
    print(x,"Unmatch open-close")
if(mystack.close and mystack.unmatch is False):
    print(x,"close paren excess")
if(mystack.open):
    print(x,"open paren excess  " ,mystack.size(),":", mystack.getValue())
if(mystack.open is False and mystack.unmatch is False and mystack.close is False):
    print(x,"MATCH")