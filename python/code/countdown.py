number = input('enter number : ')

def checktype(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

if checktype(number):
    def countdown(number):
        while number>0:
            print(number)
            number-=1
        print('blst')
    countdown(int(number))
else:
    print('enter number')