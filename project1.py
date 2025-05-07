decimal = int(input("Enter in a decimal number: "))
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary = str(remainder) + binary
    return binary