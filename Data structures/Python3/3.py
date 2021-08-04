class Stack:
    def __init__(self):
        self.myStack = list()

    def push(self, value):
        self.myStack.append(value)

    def pop(self):
        return self.myStack.pop()

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def size(self):
        return len(self.myStack)

def postFixeval(st):

    s = Stack()

    for i in range(len(st)):
        if(st[i] == "+" or st[i] == "-" or st[i] == "*" or st[i] == "/"):
            last = s.pop()
            first = s.pop()
            if(st[i] == "+"):
                s.push(first+last)
            if(st[i] == "-"):
                s.push(first-last)
            if(st[i] == "*"):
                s.push(first*last)
            if(st[i] == "/"):
                s.push(first/last)

        else:
            s.push(int(st[i]))
        #print(s.myStack)

    ### Enter Your Code Here ###

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

#print(token)

#postFixeval(token)

print("Answer : ",'{:.2f}'.format(postFixeval(token)))

"""
6 5 2 3 + 8 * - 3 + *

((6 * ((5 - ((2 + 3) * 8)) + 3)))

"""