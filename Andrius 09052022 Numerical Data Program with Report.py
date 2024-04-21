# Function to simulate OR Gate
def OR(A, B):
    return A | B

# Function to simulate AND Gate
def AND(A, B):
    return A & B

# Function to simulate XOR Gate
def XOR(A, B):
    return A ^ B

def dec2bin(num):
    res = []
    while num >= 1:
        res.append(num % 2)
        num = num // 2
    res.reverse()
    return res
# byte addition operation
def byteadder(a,b):
    C = 0
    idx = len(a) -1
    
    res = []
    while idx >= 0:
        s = XOR(XOR(a[idx], b[idx]),C)
        C = OR(AND(a[idx], b[idx]),AND(XOR(a[idx], b[idx]), C))
        idx = idx -1
        res.append(s)
    res.append(C)
    res.reverse()
    return res
# validation checking function
def checkvalid(num,fmt):
    valid = False
    if fmt == 'b':
        if num.isdigit():
            s = {'0', '1'}
            if (len(num) <= 8) and ((s == set(num)) or (set(num) == {'0'}) or (set(num) == {'1'})):
                valid = True; num = list(map(lambda x: int(x), num))
            else:
                print('Invalid binary number. Either all digits are not binary or length of binary number is more than 8 bits.')
        else:
            print('Invalid binary number.')
    elif fmt == 'd':
        if num.isdigit():
            if int(num) <= 255:
                valid = True; num = dec2bin(int(num))
            else:
                print('Decimal number is over 255. It must be between 0 and 255.')
        else:
            print('Invalid decimal number.')
    else:
        print('Invalid format of number specified. It must be one of binary or decimal (b or d).')
        valid = False; 
    return valid,num

print('******Welcome to bit addition calculator******')
uinp = 'y' # setting userinput intially to y
# looping until user want to perform additions
while uinp == 'y':
    uinp = input('Press y to calculate addition of two positive integers or type any other key to exit program:')
    if uinp == 'y':                
        valinp1 = False; valinp2 = False # setting the validation logic of both number to false
        # constantly asking user for input of numbers till at least one number is invalid
        while not (valinp1 and valinp2):
            f1 = input('Please enter the format of first positive integer number (b=binary or d=decimal): ')
            inp1 = input('Please input first integer number:')
            valinp1,num1 = checkvalid(inp1,f1)
            
            f2 = input('Please enter the format of first positive integer number (b=binary or d=decimal): ')
            inp2 = input('Please input second integer number:')
            valinp2,num2 = checkvalid(inp2,f2)
            # case when two numbers are valid
            if valinp1 and valinp2:
                if len(num1) > len(num2):
                    nzero = len(num1) - len(num2)
                    num2 = [0]*nzero + num2
                    print(str(nzero)+' zero/s appended at start of second number as it is smaller in length in binary form.')
                elif len(num2) > len(num1):
                    nzero = len(num2) - len(num1)
                    num1 = [0]*nzero + num1
                    print(str(nzero)+' zero/s appended at start of first number as it is smaller in length in binary form.')
                else:
                    print('The number of digits of both numbers are same hence no zero appending required.')
                res = byteadder(num1,num2)
                res = list(map(lambda x: str(x),res))
                print('The sum of two numbers in binary form is: ', ''.join(res))
            # case when at least one of them is invalid
            else:
                print('Please re enter both numbers as at least one of the entries are invalid.')
        
    else:
        print('Program stopped by user.')

