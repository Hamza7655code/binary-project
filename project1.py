decimal = int(input("Enter a decimal number: "))
def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary
print(decimal_to_binary(decimal))
