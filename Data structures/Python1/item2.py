###multiplication or sum
''' รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 
    ให้ show ผลรวมของจำนวนทั้งสอง 
    แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง
'''
if __name__ == "__main__":
    print("*** multiplication or sum ***")
    x , y = map(int, input("Enter num1 num2 : ").split())

    if x*y <= 1000 :
        sum = x*y
        print("The result is", sum)
    else :
        sum = x+y
        print("The result is", sum)

