if __name__ == '__main__':
    print(' *** Wind classification ***')
    speed = float(input('Enter wind speed (km/h) : '))
    res = ''
    if speed < 0:
        print("!!!Wrong value can't classify.")
        quit()
    if 0 <= speed < 52:
        res = 'Breeze'
    elif speed < 56:
        res = 'Depression'
    elif speed < 102:
        res = 'Tropical Storm'
    elif speed < 209:
        res = 'Typhoon'
    elif speed >= 209:
        res = 'Super Typhoon'
    print(f'Wind classification is {res}.')

-----------------------------------------------------------------------------

if __name__ == '__main__':
    print('*** String Rotation ***')
    original = input('Enter 2 strings : ').split()
    copy1 = original[0]
    copy2 = original[1]
    counter = 1
    while True:
        temp = ''
        temp += copy1[len(copy1)-2:]+copy1[:len(copy1) -
                                           2]  # rotate 2 to the right
        copy1 = temp

        temp = ''
        temp += copy2[3:]+copy2[:3]  # rotate 3 to the left
        copy2 = temp

        if counter <= 5:
            print(counter, copy1, copy2)
        if copy1 == original[0] and copy2 == original[1]:
            if counter > 5:
                print(' . . . . .')
                print(counter, copy1, copy2)
            break
        counter += 1
    print(f'Total of  {counter} rounds.')


-------------------------------------------------------------------------------------

def factor_list(num):
    out = list()
    for i in range(1, num):
        if num % i == 0:
            out.append(i)
    return out


if __name__ == '__main__':
    print(' *** Perfect Number Verification ***')
    number = int(input('Enter number : '))
    if number < 0:
        print('Only positive number !!!')
        quit()
    else:
        lst = factor_list(number)
        if sum(lst) == number:
            print(f'{number} is a PERFECT NUMBER.')
        else:
            print(f'{number} is NOT a perfect number.')
        print('Factors :', lst)

------------------------------------------------------------------------------------
class MyInt:
    def __init__(self, value):
        self.value = value

    def isPrime(self):
        if self.value == 2:
            return f'{self.value} isPrime : True'
        if self.value <= 1:
            return f'{self.value} isPrime : False'
        for i in range(2, 1+self.value//2):
            if self.value % i == 0:
                return f'{self.value} isPrime : False'
        return f'{self.value} isPrime : True'

    def showPrime(self):
        if self.value <= 1:
            return '!!!A prime number is a natural number greater than 1'

        def check_prime(v):
            if self.value == 2:
                return True
            if self.value == 1:
                return False
            for x in range(2, 1+v//2):
                if v % x == 0:
                    return False
            return True
        out = ''
        for i in range(2, 1+self.value):
            if check_prime(i):
                out += str(i)+" "
        return out

    def __sub__(self, obj):
        return self.value - (obj.value // 2)


def use_myint(in1, in2):
    a = MyInt(in1)
    b = MyInt(in2)
    print(a.isPrime())
    print(b.isPrime())
    print(f'Prime number between 2 and {a.value} : '+a.showPrime())
    print(f'Prime number between 2 and {b.value} : '+b.showPrime())
    print(f"{a.value} - {b.value} = {a-b}")


if __name__ == '__main__':
    print(' *** class MyInt ***')
    inp = list(map(int, input('Enter 2 number : ').split()))
    use_myint(inp[0], inp[1])

--------------------------------------------------------------------------------

if __name__ == '__main__':
    inp = list(map(int, input('Enter number end with (-1) : ').split()))
    if inp.count(-1) <= 0:
        print('Invalid INPUT !!!')
    else:
        new_inp = list()
        for i in inp:
            if i == -1:
                break
            new_inp.append(i)
        if new_inp != []:
            inp = new_inp
            ans = dict()
            set_inp = set(inp)
            for i in set_inp:
                ans[i] = inp.count(i)

            m = 0
            key_ans = 0
            all_freq = 0
            for k, v in ans.items():
                all_freq += v
                if v > m:
                    m = v
                    key_ans = k
            if ans[key_ans] > all_freq/2:
                print(key_ans)
            else:
                print('Not found')
        else:
            print('Not found')

----------------------------------------------------------------------------------

