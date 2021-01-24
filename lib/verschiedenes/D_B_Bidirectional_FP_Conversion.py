# Function converts the value passed as parameter to it's decimal representation
# First we take the integer part from the floating point value and convert it to binary then
# take fractional part and convert it to binary form and lastly combining both.
def float_bin(i, places=3):
    my_whole, my_dec = str(i).split(".")
    my_whole = int(my_whole)
    my_dec = int(my_dec)
    res = bin(my_whole).lstrip("0b") + "."
    for x in range(places):
        my_whole, my_dec = str((my_decimal_converter(my_dec)) * 8).split(".")
        my_dec = int(my_dec)
        res += my_whole
    return res


def my_decimal_converter(num):
    while num > 1:
        num /= 10
    return num


# Function converts the value passed as parameter to it's binary representation
def bin2float(b):
    s, f = b.find('.') + 1, int(b.replace('.', ''), 2)
    return f / 2. ** (len(b) - s) if s else f


# Driver Code
choice = int(input("Enter 1 for a decimal and 2 for binary input value : \n"))
if choice == int(1):
    i = float(input("Enter your decimal floating point value (e.g. 10.2) : \n"))
    p = int(input("Enter the number of decimal places of the result (some numbers may not work) : \n"))
    print('Decimal to Binary floating point conversion', i, '-->', float_bin(i, places=p))
elif choice == int(2):
    i = str(input("Enter your binary floating point value (e.g. 10.10) : \n"))
    print('Binary to Decimal floating point conversion', i, '-->', bin2float(i))
else:
    print('Invalid choice. Please start application again.')
