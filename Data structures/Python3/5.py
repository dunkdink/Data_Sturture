###จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

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

def dec2bin(decnum):
    s = Stack()
    if(decnum == 0):
        s.push(0)
    else:
        while(decnum > 0):
            s.push(decnum % 2)
            decnum = decnum // 2
    
    ans = ""
    while(not s.isEmpty()):
        ans = ans + str(s.pop())

    return ans

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))