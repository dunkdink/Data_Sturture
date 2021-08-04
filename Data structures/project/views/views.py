from django.db.models.expressions import F
from django.shortcuts import render,redirect
from django.http import HttpResponse
from DataStructProject import urls
from .models import AllClassRooM
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib import messages
import datetime
from django.utils.timezone import utc
import time
# Create your views here.


""" Creat a Suitable Class"""

class Stack:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def peek2(self):
        return self.items[-2]
    def peekFull(self):
        return self.items

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
        if prev is None:
            self.prev = None
        else:
            self.prev = prev

    def __str__(self):
        return str(self.data)



class DoublyLk:
    def __init__(self):
        self.font = Node(None)
        self.back = Node(None)
        self.head = self.font
        self.tail = self.back
        self.font.next = self.back
        self.font.prev = None
        self.back.prev = self.font
        self.back.next = None
    def __str__(self):
        t = self.font
        strt = ""
        if t.next is None:
            return strt
        else:
            while t.next is not self.back:
                t = t.next
                strt += str(t.data) + " "
            return strt

    def getlst(self):
        lis = []
        t = self.font
        if t.next is None:
            return lis
        else:
            while t.next is not self.back:
                t = t.next
                lis.append(t.data)
            return lis

    def reversedStr(self):
        t = self.back
        strt = ""
        if t.prev is self.font:
            return strt
        else:
            while t.prev != self.font:
                t = t.prev
                strt += str(t.data) + " "
            return strt

    def isEmpty(self):
        return self.font.next == None

    def size(self):
        t = self.font
        count = 0
        if self.isEmpty():
            return count
        else:
            while t.next is not self.back:
                t = t.next
                count += 1
            return count                    

    def append(self,data):
        t = self.font
        p = Node(data)
        if self.isEmpty():
            self.font.next = p
            p.prev = self.font
            self.back.prev = p
            p.next = self.back
        else:
            while t != self.back:
                t = t.next
            p.next = self.back
            p.prev = self.back.prev
            self.back.prev.next = p
            self.back.prev = p

    def addHead(self, data):
        t = self.font
        p = Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            p.next = self.font.next
            p.prev = self.font
            self.font.next.prev = p
            self.font.prev = None
            self.font.next = p

    def search(self, data):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return "Not Found"
        else:
            while t.next is not self.back:
                if t.data == data:
                    return count
                else:
                    t = t.next
                    count += 1
            if t.data == data:
                return count
            else:
                return "Not Found"

    def index(self, items):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return -1
        else:
            while t is not self.back:
                if t.data == items:
                    return count
                else:
                    t = t.next
                    count += 1
            return count 

    def pop(self, index):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return "Empty"
        else:
            while t is not self.back:
                if self.index(t.data) == index:
                    break
                else:
                    t = t.next
            if t is not self.back:
                t.prev.next = t.next
                t.next.prev = t.prev
                t.next = None
                t.prev = None
            else:
                return "Out of Range"

    def insert(self , index, data):
        t = self.font.next
        p = Node(data)
        if self.isEmpty():
            self.addHead(data)
        else:
            while t is not self.back:
                if self.index(t.data) == index:
                    break
                else:
                    t = t.next
            if t is not self.back:
                p.next = t
                p.prev = t.prev
                t.prev.next = p
                t.prev = p
            else:
                t = t.prev
                self.append(data)


class NodeBsT:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = NodeBsT(data)
        else:
            curr = self.root
            while True:
                if int(data.split()[0]) < int(curr.data.split()[0]):
                    if curr.left is None:
                        curr.left = NodeBsT(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = NodeBsT(data)
                        break
                    curr = curr.right
        return self.root

    def max(self):
        if self.root is None:
            return
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    def min(self):
        if self.root is None:
            return
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def mult(self, k, multiplier):  # bfs then multiply
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            if curr.data > k:
                curr.data = curr.data*multiplier
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

    def bfs(self):
        if self.root is None:
            return "Empty Tree"
        q = Queue()
        q.enqueue(self.root)
        out = "Breadth : "
        while not q.is_empty():
            curr = q.dequeue()
            out += str(curr.data) + ' '
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
        return out

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)


pre = 'Preorder : '
post = 'Postorder : '
allStudent = Stack()


def preorder(curr):
    global pre
    if curr is not None:
        pre += str(curr.data) + ' '
        preorder(curr.left)
        preorder(curr.right)


def inorder(curr):
    global allStudent
    if curr is not None:
        inorder(curr.left)
        allStudent.push(curr.data)
        inorder(curr.right)


def postorder(curr):
    global post
    if curr is not None:
        postorder(curr.left)
        postorder(curr.right)
        post += str(curr.data)+' '


def partitionMin(arr, low, high):
    i = (low-1)  
    a = arr[high].split()
    pivot = int(a[0]) 
  
    for j in range(low, high):
        r = arr[j].split()
        if int(r[0]) <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def partitionMax(arr, low, high):
    i = (low-1)  
    a = arr[high].split()
    pivot = int(a[0]) 
  
    for j in range(low, high):
        r = arr[j].split()
        if int(r[0]) >= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def partitionMaxDay(arr, low, high):
    i = (low-1)     # index of smaller element
    a = arr[high].split()
    m = a[5].split('/')
    n = a[6].split(':')
    pivotY = int(m[2])    # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        r = arr[j].split()
        l = r[5].split('/')
        k = r[6].split(':')
        if int(l[2]) == pivotY:
            pivotM = int(m[1])
            if int(l[1]) == pivotM:
                pivotD = int(m[0])
                if int(l[0]) == pivotD:
                    pivotHr = int(n[0])
                    if int(k[0]) == pivotHr:
                        pivotMin = int(n[1])
                        if int(k[1]) == pivotMin:
                            pivotSec = int(n[2])
                            if int(k[2]) >= pivotSec:
                                i = i+1
                                arr[i], arr[j] = arr[j], arr[i]
                        else:
                            if int(k[1]) >= pivotMin:
                                i = i+1
                                arr[i], arr[j] = arr[j], arr[i]
                    else:
                        if int(k[0]) >= pivotHr:
                            i = i+1
                            arr[i], arr[j] = arr[j], arr[i]  
                else:
                    if int(l[0]) >= pivotD:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]  
            else:
                if int(l[1]) >= pivotM:
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
        else:
            if int(l[2]) >= pivotY:
    
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def partitionMinDay(arr, low, high):
    i = (low-1)     # index of smaller element
    a = arr[high].split()
    m = a[5].split('/')
    n = a[6].split(':')
    pivotY = int(m[2])    # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        r = arr[j].split()
        l = r[5].split('/')
        k = r[6].split(':')
        if int(l[2]) == pivotY:
            pivotM = int(m[1])
            if int(l[1]) == pivotM:
                pivotD = int(m[0])
                if int(l[0]) == pivotD:
                    pivotHr = int(n[0])
                    if int(k[0]) == pivotHr:
                        pivotMin = int(n[1])
                        if int(k[1]) == pivotMin:
                            pivotSec = int(n[2])
                            if int(k[2]) <= pivotSec:
                                i = i+1
                                arr[i], arr[j] = arr[j], arr[i]
                        else:
                            if int(k[1]) <= pivotMin:
                                i = i+1
                                arr[i], arr[j] = arr[j], arr[i]
                    else:
                        if int(k[0]) <= pivotHr:
                            i = i+1
                            arr[i], arr[j] = arr[j], arr[i]  
                else:
                    if int(l[0]) <= pivotD:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]  
            else:
                if int(l[1]) <= pivotM:
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
        else:
            if int(l[2]) <= pivotY:
    
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

  
def quickSort(arr, low, high, isMM):
    if len(arr) == 1:
        return arr
    if low < high:
        if isMM == 0:
            pi = partitionMin(arr, low, high)
        elif isMM == 2:
            pi = partitionMinDay(arr, low, high)
        elif isMM == 3:
            pi = partitionMaxDay(arr, low, high)
        else:
            pi = partitionMax(arr, low, high)
        quickSort(arr, low, pi-1, isMM)
        quickSort(arr, pi+1, high, isMM)

def bi_search(left, right, lst, key):
    if left <= right:
        mid = (left + right) // 2
        if int(lst[mid].split()[0]) < int(key):
            return bi_search(mid + 1, right, lst, key)
        elif int(lst[mid].split()[0]) > int(key):
            return bi_search(left, mid - 1, lst, key)
        else:
            return lst[mid]
    return False
  
  
  

""" Initial """
buffer = Stack()
buffer2 = Stack()
buffer3 = Stack()
buffer4 = Stack()
buffer5 = Stack()
buffer6 = Stack()
# allStudent = Stack()
allStudentBST = BST()
allStudentDataBase_Stack = Stack()
allId = Stack()
#studentInData = Stack()
studentInData = DoublyLk()
studentInComnet = DoublyLk()
studentInComOrg = DoublyLk()
studentInEpp = DoublyLk()
studentInProb = DoublyLk()
allClassIndex = [studentInData,studentInComnet,studentInComOrg,studentInEpp,studentInProb]
addFormed = False
datafileisEmpty = False
comNetfileisEmpty = False
comOrgfileisEmpty = False
ePPfileisEmpty = False
probfileisEmpty = False


"""" Read TXT File"""





######################################################################################## ตรวจว่า file ว่างรึเปล่า ####################################################################
fl = open('studentInData.txt', encoding="utf8")
while True:
    s = fl.readline()
    if s == '':
        break
    for i in s.split(','):
        if i == '':
            pass
        else:
            buffer2.push(i)
fl.close()

cnl = open('studentInComnet.txt', encoding="utf8")
while True:
    s = cnl.readline()
    if s == '':
        break
    for i in s.split(','):
        if i == '':
            pass
        else:
            buffer3.push(i)
cnl.close()

col = open('studentInComOrg.txt', encoding="utf8")
while True:
    s = col.readline()
    if s == '':
        break
    for i in s.split(','):
        if i == '':
            pass
        else:
            buffer4.push(i)
col.close()
    

epl = open('studentInEpp.txt', encoding="utf8")
while True:
    s = epl.readline()
    if s == '':
        break
    for i in s.split(','):
        if i == '':
            pass
        else:
            buffer5.push(i)
epl.close()

prl = open('studentInProb.txt', encoding="utf8")
while True:
    s = prl.readline()
    if s == '':
        break
    for i in s.split(','):
        if i == '':
            pass
        else:
            buffer6.push(i)
prl.close()

allFile = ['studentInData.txt','studentInComnet.txt','studentInComOrg.txt','studentInEpp.txt','studentInProb.txt']


######################################################################################## ตรวจว่า file ว่างรึเปล่า ####################################################################

if buffer2.isEmpty():
    datafileisEmpty = True
else:
    pass

if buffer3.isEmpty():
    comNetfileisEmpty = True
else:
    pass

if buffer4.isEmpty():
    comOrgfileisEmpty = True
else:
    pass

if buffer5.isEmpty():
    ePPfileisEmpty = True
else:
    pass

if buffer6.isEmpty():
    probfileisEmpty = True
else:
    pass


######################################################################################## ตรวจว่า file ว่างรึเปล่า ####################################################################


######################################################################################## Upload file เข้า Stack ##################################################################

if datafileisEmpty == False:
    rl = open('studentInData.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            break
        for i in s.split(','):
            if i == '':
                pass
            else:
                studentInData.append(i)
    rl.close()
else:
    pass



if comNetfileisEmpty == False:
    rl = open('studentInComnet.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            break
        for i in s.split(','):
            if i == '':
                pass
            else:
                studentInComnet.append(i)
    rl.close()
else:
    pass

if comOrgfileisEmpty == False:
    rl = open('studentInComOrg.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            break
        for i in s.split(','):
            if i == '':
                pass
            else:
                studentInComOrg.append(i)
    rl.close()
else:
    pass

if ePPfileisEmpty == False:
    rl = open('studentInEpp.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            print("hi")
            break
        for i in s.split(','):
            if i == '':
                pass
            else:
                studentInEpp.append(i)
    rl.close()
else:
    pass

if probfileisEmpty == False:
    rl = open('studentInProb.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            print("hi")
            break
        for i in s.split(','):
            if i == '':
                pass
            else:
                studentInProb.append(i)
    rl.close()
else:
    pass

######################################################################################## Upload file เข้า Stack ##################################################################

User = get_user_model()
users = User.objects.all()
userlist = User.objects.values()
allnameINsql = []
i = 1
while i < len(userlist):
    if userlist[i]['is_staff'] == 1:
        pass
    else:
        name = str(userlist[i]['first_name']) + " " + str(userlist[i]['last_name']) 
        idS = userlist[i]['id']
        nd = str(idS) + " " + str(name)
        allnameINsql.append(nd)
    i += 1
f = open('mySQLallstudent.txt', 'w', encoding="utf8")
for i in allnameINsql:
    f.write(i + ',')
f.close()



f = open('mySQLallstudent.txt', encoding="utf8")
while True:
    s = f.readline()
    if s == '': # check file end
        break
    for i in s.split(','):
        if i == '':
            pass
        else:
            buffer.push(i)
f.close()
print(buffer.items)
for i in buffer.items:
    a = i.split()
    if i == '':
        pass
    else:
        ID = a[0]
        nameS = a[1]
        surName = a[2]
        fullName = str(ID) + " " + str(nameS) + " " + str(surName)
        allStudentBST.insert(fullName)
    if allStudent.isEmpty():
        pass
    else:
        while not allStudent.isEmpty():
            allStudent.pop()
    inorder(allStudentBST.root)
for i in buffer.items:
    allId.push(i[0])



def updateStudentData():
    temp = Stack()
    f = open('mySQLallstudent.txt', encoding="utf8")
    while True:
        s = f.readline()

        if s == '': # check file end
            break
        for i in s.split(','):
            if i == '':
                pass
            else:
                temp.push(i)
    f.close()
    for i in temp.items:
        ID = i[0]
        nameS = i[1]
        surName = i[2]
        fullName = str(ID) + " " + str(nameS) + " " + str(surName)
        allStudentBST.insert(fullName)
        if allStudent.isEmpty():
            pass
        else:
            while not allStudent.isEmpty():
                allStudent.pop()
        inorder(allStudentBST.root)
    if allId.isEmpty():
        pass
    else:
        while not allId.isEmpty():
            allId.pop()
    for i in temp.items:
        allId.push(i[0])

def readClassStatus(txtfile):
    isStart = ""
    f = open(txtfile, encoding="utf8")
    while True:
        s = f.readline()
        if s == '':
            break
        isStart = str(s)
        if isStart == "False":
            isStart = False
        elif isStart == 'True':
            isStart = True
    f.close()
    return isStart


####################################################################################### Views CoreFunction #############################################################################################

def loginForm(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request,'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    #check user and pass
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request,user)
        f = open('nowUser.txt', 'w', encoding="utf8")
        if user.is_staff == 1:
            f.write(str(user.id) + " " + str(user.first_name) + " " + str(user.last_name) + " " + "Teach")
        else:
            f.write(str(user.id) + " " + str(user.first_name) + " " + str(user.last_name))
        print('Writing to file completed')
        f.close()
        return redirect('/home')
    else:
        messages.info(request,'User not FOUND')
        return redirect('/')

def logout(request):
    f = open('nowUser.txt', 'w', encoding="utf8")
    f.write("")
    print('Writing to file completed')
    f.close()
    auth.logout(request)
    return redirect('/home')


def information(request):
    numinclass = allStudent.size()
    return render(request,'index.html',
    {
        'className':'Data Structure 2564',
        'student':'62010465 นรวิชญ์ อยู่บัว',
        'numinClass':numinclass
    })


def allStudentName(request):
    return render(request,'allstudent.html',
    {
        'allStudent':allStudent.items
    })

def searchInAllStudent(request):
    idS = request.POST['studentID']
    if idS == "":
        return redirect('/classStatus')
    else:
        IDD = bi_search(0, len(allStudent.items) - 1, sorted(allStudent.items), int(idS))
        if IDD == False:
            messages.info(request,'Not Found')
            return redirect('/classStatus')
        else:
            name = str(IDD.split()[1] + " " + IDD.split()[2])
            User = get_user_model()
            users = User.objects.all()
            userlist = User.objects.values()
            thisEmail = ''
            nowClass = 999
            studyIn = ""
            j = 0
            while j < len(allClassIndex):
                for k in allClassIndex[j].getlst():
                    a = k.split()
                    if str(a[0]) == str(IDD.split()[0]):
                        nowClass = j
                        break
                j += 1
            i = 1
            while i < len(userlist):
                if int(userlist[i]['id']) == int(IDD.split()[0]):
                    thisEmail += str(userlist[i]['email'])
                    break
                i += 1
            if nowClass == 0:
                studyIn = "DataStruct"
            elif nowClass == 1:
                studyIn = "Computer Network"
            elif nowClass == 2:
                studyIn = "Computer Organize"
            elif nowClass == 3:
                studyIn = "English for professional purpose"
            elif nowClass == 4:
                studyIn = "Probability and Statistic"
            else:
                studyIn = "None"
            return render(request, 'thisUserData.html',{'name':name,'id':idS,'email':thisEmail,'studyIn':studyIn})


def dataStructlogin(request):
    isStart = readClassStatus("isStartData.txt")
    return render(request,'dataStructlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInData':studentInData.getlst(),'isStart':isStart})

def dataStructStart(request):
    f = open('isStartData.txt', 'w', encoding="utf8")
    f.write("True")
    print('Writing to file completed')
    f.close()
    return redirect('/dataStructlogin')

def comNetlogin(request):
    isStart = readClassStatus("isStartNet.txt")
    return render(request,'comNetlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComnet':studentInComnet.getlst(), 'isStart':isStart})

def comNetStart(request):
    f = open('isStartNet.txt', 'w', encoding="utf8")
    f.write("True")
    print('Writing to file completed')
    f.close()
    return redirect('/comNetlogin')

def comOrglogin(request):
    isStart = readClassStatus("isStartOrg.txt")
    return render(request,'comOrglogin.html',{'allStudent':allStudent.items,'addFormed':addFormed,'studentInComOrg':studentInComOrg.getlst(),'isStart':isStart})

def comOrgStart(request):
    f = open('isStartOrg.txt', 'w', encoding="utf8")
    f.write("True")
    print('Writing to file completed')
    f.close()
    return redirect('/comOrglogin')

def ePPlogin(request):
    isStart = readClassStatus("isStartEpp.txt")
    return render(request,'epplogin.html',{'allStudent':allStudent.items,'addFormed':addFormed,'studentInEpp':studentInEpp.getlst(),'isStart':isStart})

def ePPStart(request):
    f = open('isStartEpp.txt', 'w', encoding="utf8")
    f.write("True")
    print('Writing to file completed')
    f.close()
    return redirect('/epplogin')



def problogin(request):
    isStart = readClassStatus("isStartProb.txt")
    return render(request,'problogin.html',{'allStudent':allStudent.items,'addFormed':addFormed,'studentInProb':studentInProb.getlst(),'isStart':isStart})

def probStart(request):
    f = open('isStartProb.txt', 'w', encoding="utf8")
    f.write("True")
    print('Writing to file completed')
    f.close()
    return redirect('/problogin')

def test(request):
    data = AllClassRooM.objects.all()
    return render(request,'test.html',{'AllClassRooM':data})

def readNowUser():
    wholePartUser = ''
    nowUser = ''
    nowidS = ''
    fl = open('nowUser.txt', encoding="utf8")
    while True:
        s = fl.readline()
        if s == '':
            break
        wholePartUser += str(s)
    fl.close()
    if wholePartUser == '':
        pass
    elif len(wholePartUser.split()) > 3:
        return nowidS,nowUser,1
    else:
        nowidS = wholePartUser.split()[0]
        nowUser = wholePartUser.split()[1] + " " + wholePartUser.split()[2]
        return nowidS,nowUser,0



########################################################################## ส่วน login Data ############################################################################################

def visualize(inOut,idS,name,htmlFile,studentIN,allFilenIndex):
    registerSucess = False
    alreadyRegister = False
    alreadyInOtherClass = False
    addFormed = True
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%d/%m/%Y %H:%M:%S", named_tuple)
    # idS = request.POST['studentID']
    # name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return 1,alreadylogin,noInDataBase,addFormed,alreadyRegister,registerSucess,alreadyInOtherClass
    else:
        idandNameOnly = str(idS) + " " + str(name)
        timePlusIdname = str(idS) + " " + str(name) + " login at " + " " + str(time_string)
        alreadylogin = False
        noInDataBase = False
        classEmpty = False

        if studentIN.isEmpty():
            classEmpty = True
        else:
            pass
        for i in studentIN.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
                break
            else:
                pass
        for i in allClassIndex:
            for j in i.getlst():
                a = j.split()
                if a[0] == idS:
                    alreadyInOtherClass = True
                    break
                else:
                    pass
        if inOut == 1:
            if alreadylogin == False and noInDataBase == False and alreadyInOtherClass == False:
                if studentIN.isEmpty():
                    f = open(allFile[allFilenIndex], 'a', encoding="utf8")
                    f.write(timePlusIdname + ',')
                    print('Writing to file completed')
                    f.close()
                    studentIN.append(timePlusIdname)
                else:
                    f = open(allFile[allFilenIndex], 'a', encoding="utf8")
                    f.write(timePlusIdname + ',')
                    print('Writing to file completed')
                    f.close()
                    studentIN.append(timePlusIdname)
                addFormed = False
            else:
                pass
        else:
            if alreadylogin == True and noInDataBase == False:
            # f = open('studentInData.txt', 'a', encoding="utf8")
            # f.write(timePlusIdname + '\n')
            # print('Writing to file completed')
            # f.close()
            # studentInData.push(timePlusIdname)
                if classEmpty == True:
                    pass
                else:
                    for i in studentIN.getlst():
                        a = i.split()
                        if a[0] == idS:
                            studentIN.pop(studentIN.search(i))
                    f = open(allFile[allFilenIndex], 'w', encoding="utf8")
                    for i in studentIN.getlst():
                        f.write(i + ',')
                    f.close()
                    addFormed = False
            else:
                pass
        return 0,alreadylogin,noInDataBase,addFormed,alreadyRegister,registerSucess,alreadyInOtherClass


def dataStructloginAddIDandName(request):
    isStart = readClassStatus("isStartData.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    thislis = []
    thislis = visualize(1,idS,name,'dataStructlogin.html',studentInData,0)
    return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})


def dataStructlogout(request):
    isStart = readClassStatus("isStartData.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    if readNowUser()[2] == 1:
        idS = request.POST['studentID']
        name = 'kick'
    thislis = []
    thislis = visualize(0,idS,name,'dataStructlogin.html',studentInData,0)
    return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def dataEndClass(request):
    thislis = []
    f = open('isStartData.txt', 'w', encoding="utf8")
    f.write("False")
    print('Writing to file completed')
    f.close()
    isStart = False
    if len(studentInData.getlst()) == 0:
        return redirect('/dataStructlogin')
    else:
        for i in studentInData.getlst():
            a = i.split()
            idS = a[0]
            name = a[1]
            thislis = visualize(0,idS,name,'dataStructlogin.html',studentInData,0)
        return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})



def dataMinMaxID(request):
    isStart = readClassStatus("isStartData.txt")
    arr = []
    arr = studentInData.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 0)
    print(arr)
    return render(request,'dataStructlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInData':arr,'isStart':isStart})

def dataMaxMinID(request):
    isStart = readClassStatus("isStartData.txt")
    arr = []
    arr = studentInData.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 1)
    print(arr)
    return render(request,'dataStructlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInData':arr,'isStart':isStart})

def dataMinMaxDay(request):
    isStart = readClassStatus("isStartData.txt")
    arr = []
    arr = studentInData.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 2)
    print(arr)
    return render(request,'dataStructlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInData':arr,'isStart':isStart})

def dataMaxMinDay(request):
    isStart = readClassStatus("isStartData.txt")
    arr = []
    arr = studentInData.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 3)
    print(arr)
    return render(request,'dataStructlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInData':arr,'isStart':isStart})




    
########################################################################## ส่วน login Data ############################################################################################

########################################################################## ส่วน login Comnet ############################################################################################
def comNetloginAddIDandName(request):
    isStart = readClassStatus("isStartNet.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    thislis = []
    thislis = visualize(1,idS,name,'comNetlogin.html',studentInComnet,1)
    return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def comNetlogout(request):
    isStart = readClassStatus("isStartNet.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    if readNowUser()[2] == 1:
        idS = request.POST['studentID']
        name = 'kick'
    thislis = []
    thislis = visualize(0,idS,name,'comNetlogin.html',studentInComnet,1)
    return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def comNetEndClass(request):
    thislis = []
    f = open('isStartNet.txt', 'w', encoding="utf8")
    f.write("False")
    print('Writing to file completed')
    f.close()
    isStart = False
    if len(studentInComnet.getlst()) == 0:
        return redirect('/comNetlogin')
    else:
        for i in studentInComnet.getlst():
            a = i.split()
            idS = a[0]
            name = a[1]
            thislis = visualize(0,idS,name,'comNetlogin.html',studentInComnet,1)
        return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def comNetMinMaxID(request):
    isStart = readClassStatus("isStartNet.txt")
    arr = []
    arr = studentInComnet.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 0)
    print(arr)
    return render(request,'comNetlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComnet':arr,'isStart':isStart})

def comNetMaxMinID(request):
    isStart = readClassStatus("isStartNet.txt")
    arr = []
    arr = studentInComnet.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 1)
    print(arr)
    return render(request,'comNetlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComnet':arr,'isStart':isStart})

def comNetMinMaxDay(request):
    isStart = readClassStatus("isStartNet.txt")
    arr = []
    arr = studentInComnet.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 2)
    print(arr)
    return render(request,'comNetlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComnet':arr,'isStart':isStart})

def comNetMaxMinDay(request):
    isStart = readClassStatus("isStartNet.txt")
    arr = []
    arr = studentInComnet.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 3)
    print(arr)
    return render(request,'comNetlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComnet':arr,'isStart':isStart})
            

########################################################################## ส่วน login Comnet ############################################################################################

########################################################################## ส่วน login ComOrg ############################################################################################

def comOrgloginAddIDandName(request):
    isStart = readClassStatus("isStartOrg.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    thislis = []
    thislis = visualize(1,idS,name,'comOrglogin.html',studentInComOrg,2)
    return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def comOrglogout(request):
    isStart = readClassStatus("isStartOrg.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    if readNowUser()[2] == 1:
        idS = request.POST['studentID']
        name = 'kick'
    thislis = []
    thislis = visualize(0,idS,name,'comOrglogin.html',studentInComOrg,2)
    return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def comOrgEndClass(request):
    thislis = []
    f = open('isStartOrg.txt', 'w', encoding="utf8")
    f.write("False")
    print('Writing to file completed')
    f.close()
    isStart = False
    if len(studentInComOrg.getlst()) == 0:
        return redirect('/comOrglogin')
    else:
        for i in studentInComOrg.getlst():
            a = i.split()
            idS = a[0]
            name = a[1]
            thislis = visualize(0,idS,name,'comOrglogin.html',studentInComOrg,2)
        return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def comOrgMinMaxID(request):
    isStart = readClassStatus("isStartOrg.txt")
    arr = []
    arr = studentInComOrg.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 0)
    print(arr)
    return render(request,'comOrglogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComOrg':arr,'isStart':isStart})

def comOrgMaxMinID(request):
    isStart = readClassStatus("isStartOrg.txt")
    arr = []
    arr = studentInComOrg.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 1)
    print(arr)
    return render(request,'comOrglogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComOrg':arr,'isStart':isStart})

def comOrgMinMaxDay(request):
    isStart = readClassStatus("isStartOrg.txt")
    arr = []
    arr = studentInComOrg.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 2)
    print(arr)
    return render(request,'comOrglogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComOrg':arr,'isStart':isStart})

def comOrgMaxMinDay(request):
    isStart = readClassStatus("isStartOrg.txt")
    arr = []
    arr = studentInComOrg.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 3)
    print(arr)
    return render(request,'comOrglogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComOrg':arr,'isStart':isStart})
  

########################################################################## ส่วน login Comorg ############################################################################################

########################################################################## ส่วน login Epp ############################################################################################

def ePPloginAddIDandName(request):
    isStart = readClassStatus("isStartEpp.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    thislis = []
    thislis = visualize(1,idS,name,'epplogin.html',studentInEpp,3)
    return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def ePPlogout(request):
    isStart = readClassStatus("isStartEpp.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    if readNowUser()[2] == 1:
        idS = request.POST['studentID']
        name = 'kick'
    thislis = []
    thislis = []
    thislis = visualize(0,idS,name,'epplogin.html',studentInEpp,3)
    return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def ePPEndClass(request):
    thislis = []
    f = open('isStartEpp.txt', 'w', encoding="utf8")
    f.write("False")
    print('Writing to file completed')
    f.close()
    isStart = False
    if len(studentInEpp.getlst()) == 0:
        return redirect('/epplogin')
    else:
        for i in studentInEpp.getlst():
            a = i.split()
            idS = a[0]
            name = a[1]
            thislis = visualize(0,idS,name,'epplogin.html',studentInEpp,3)
        return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})


def ePPMinMaxID(request):
    isStart = readClassStatus("isStartEpp.txt")
    arr = []
    arr = studentInEpp.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 0)
    print(arr)
    return render(request,'epplogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInEpp':arr,'isStart':isStart})

def ePPMaxMinID(request):
    isStart = readClassStatus("isStartEpp.txt")
    arr = []
    arr = studentInEpp.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 1)
    print(arr)
    return render(request,'epplogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInEpp':arr,'isStart':isStart})

def ePPMinMaxDay(request):
    isStart = readClassStatus("isStartEpp.txt")
    arr = []
    arr = studentInEpp.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 2)
    print(arr)
    return render(request,'epplogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInEpp':arr,'isStart':isStart})

def ePPMaxMinDay(request):
    isStart = readClassStatus("isStartEpp.txt")
    arr = []
    arr = studentInEpp.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 3)
    print(arr)
    return render(request,'epplogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInEpp':arr,'isStart':isStart})
    
########################################################################## ส่วน login Epp ############################################################################################


########################################################################## ส่วน login Prob ############################################################################################

def probloginAddIDandName(request):
    isStart = readClassStatus("isStartProb.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    thislis = []
    thislis = visualize(1,idS,name,'problogin.html',studentInProb,4)
    return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def problogout(request):
    isStart = readClassStatus("isStartProb.txt")
    idS = readNowUser()[0]
    name = readNowUser()[1]
    if readNowUser()[2] == 1:
        idS = request.POST['studentID']
        name = 'kick'
    thislis = []
    thislis = []
    thislis = visualize(0,idS,name,'problogin.html',studentInProb,4)
    return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})

def probEndClass(request):
    thislis = []
    f = open('isStartProb.txt', 'w', encoding="utf8")
    f.write("False")
    print('Writing to file completed')
    f.close()
    isStart = False
    if len(studentInProb.getlst()) == 0:
        return redirect('/problogin')
    else:
        for i in studentInProb.getlst():
            a = i.split()
            idS = a[0]
            name = a[1]
            thislis = visualize(0,idS,name,'problogin.html',studentInProb,4)
        return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':thislis[1],'noInDataBase':thislis[2],'addFormed':thislis[3],
        'alreadyRegister':thislis[4],'registerSucess':thislis[5],'alreadyInOtherClass':thislis[6],'isStart':isStart})


def probMinMaxID(request):
    isStart = readClassStatus("isStartProb.txt")
    arr = []
    arr = studentInProb.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 0)
    print(arr)
    return render(request,'problogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInProb':arr,'isStart':isStart})

def probMaxMinID(request):
    isStart = readClassStatus("isStartProb.txt")
    arr = []
    arr = studentInProb.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 1)
    print(arr)
    return render(request,'problogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInProb':arr,'isStart':isStart})

def probMinMaxDay(request):
    isStart = readClassStatus("isStartProb.txt")
    arr = []
    arr = studentInProb.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 2)
    print(arr)
    return render(request,'problogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInProb':arr,'isStart':isStart})

def probMaxMinDay(request):
    isStart = readClassStatus("isStartProb.txt")
    arr = []
    arr = studentInProb.getlst().copy()
    n = len(arr)
    quickSort(arr, 0, n-1, 3)
    print(arr)
    return render(request,'problogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInProb':arr,'isStart':isStart})


########################################################################## ส่วน login Prob ############################################################################################


########################################################################## Register ###############################################################


def userInformation(request):
    User = get_user_model()
    users = User.objects.all()
    userlist = User.objects.values()
    thisEmail = ''
    nowClass = 999
    studyIn = ""
    name = readNowUser()[1]
    idS = readNowUser()[0]
    j = 0
    while j < len(allClassIndex):
        for k in allClassIndex[j].getlst():
            a = k.split()
            if str(a[0]) == str(readNowUser()[0]):
                nowClass = j
                break
        j += 1
    i = 1
    while i < len(userlist):
        if int(userlist[i]['id']) == int(readNowUser()[0]):
            thisEmail += str(userlist[i]['email'])
            break
        i += 1
    print("Hiii",thisEmail)
    if nowClass == 0:
        studyIn = "DataStruct"
    elif nowClass == 1:
        studyIn = "Computer Network"
    elif nowClass == 2:
        studyIn = "Computer Organize"
    elif nowClass == 3:
        studyIn = "English for professional purpose"
    elif nowClass == 4:
        studyIn = "Probability and Statistic"
    else:
        studyIn = "None"
    return render(request, 'thisUserData.html',{'name':name,'id':idS,'email':thisEmail,'studyIn':studyIn})

def registerPage(request):
    # data = User.objects.order_by('id')
    User = get_user_model()
    users = User.objects.all()
    userlist = User.objects.values()
    allname = []
    # all_users = User.objects.values()
    # print(all_users)
    # print(all_users[0]['username'])
    i = 1
    while i < len(userlist):
        name = str(userlist[i]['first_name']) + " " + str(userlist[i]['last_name']) 
        idS = userlist[i]['id']
        nd = str(idS) + " " + str(name)
        allname.append(nd)
        i += 1
    return render(request,'registeration.html',{'allUser':allname})

def addFormedRegister(request):
    idS = request.POST['studentID']
    name = request.POST['studentName']
    username = request.POST['userName']
    surname = request.POST['studentSurname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'This Username is already been taken !!')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'This Email is already been registered !!')
            return redirect('/register')
        else:
            user = User.objects.create_user(
            id = idS,
            username = username,
            password = password,
            first_name = name,
            last_name = surname,
            email = email
            )
            user.save()
            wholePart = str(idS) + " " + str(name) + " " + str(surname)
            f = open("mySQLallstudent.txt", 'a', encoding="utf8")
            f.write(wholePart + ',')
            print('Writing to file completed')
            f.close()
            allStudentBST.insert(wholePart)
            while not allStudent.isEmpty():
                allStudent.pop()
            inorder(allStudentBST.root)
            return redirect('/')
    else:
        messages.info(request,'Your password does not match')
        return redirect('/register')

def registerPageAsTeach(request):
    # data = User.objects.order_by('id')
    User = get_user_model()
    users = User.objects.all()
    userlist = User.objects.values()
    allname = []
    # all_users = User.objects.values()
    # print(all_users)
    # print(all_users[0]['username'])
    i = 1
    while i < len(userlist):
        if int(userlist[i]['is_staff']) == 1: 
            name = str(userlist[i]['first_name']) + " " + str(userlist[i]['last_name'])
            print(name)
            allname.append(name)
        else:
            print("HI")
            pass
        i += 1
    return render(request,'registerationAsTeach.html',{'allUser':allname})

def addFormedRegisterAsTeach(request):
    name = request.POST['studentName']
    username = request.POST['userName']
    surname = request.POST['studentSurname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'This Username is already been taken !!')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'This Email is already been registered !!')
            return redirect('/register')
        else:
            user = User.objects.create_user(
            username = username,
            password = password,
            first_name = name,
            last_name = surname,
            email = email,
            is_staff = 1
            )
            user.save()
            return redirect('/')
    else:
        messages.info(request,'Your password does not match')
        return redirect('/registerAsTeach')

def test001(request):
    return render(request, 'test001.html')