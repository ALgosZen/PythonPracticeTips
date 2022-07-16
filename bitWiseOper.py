x = 0b101
y = bin(x >> 3) #to print binary
print(y)
y = bin(x << 3)
print(y)
print(x * x) # decimal

a = 0b11110000
b = 0b11001100
 #decimal notation
print(a)
print(b)
print(a+b)
print(bin(a) + "\n" + bin(b))
# now operators
print("AND operator: " + bin(a&b))
print("OR operator: " + bin(a|b))
print("XOR operator: " + bin(a^b))
print("Bitwise Ones Complement : " + bin(~a))
print("integer and : " + str(10&7))

#:#b -> converts to binary
#:#o -> converts to octal
#:#x -> converts to hexadecimal 
#:#0 -> converts to decimal

print("decimal value of binary: " + f'{0b11110000:#0}')
print("decimal value of binary changes by padding zeros end: " + f'{0b111100000000:#0}')

# int and eval can be used to print integer value of binary , decimal etc.,
# int(bin(a),2)
# eval(bin(a))

