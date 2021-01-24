# pip install coden
import coden

d = 24
h = "ff"
b = 100101

print('Decimal to Binary')
a_decimal_number = d
binary_output = coden.int_to_bin(a_decimal_number)
print(d, '-->', binary_output)

print('Decimal to Hexadecimal')
a_decimal_number = 165
hexadecimal_output = coden.int_to_hex(a_decimal_number)
print(d, '-->', hexadecimal_output)

print('Binary to Hexdecimal')
a_binary_number = b
hexadecimal_output = coden.bin_to_hex(a_binary_number)
print(b, '-->', hexadecimal_output)

print('Binary to Decimal')
a_binary_number = b
decimal_output = coden.bin_to_int(a_binary_number)
print(b, '-->', decimal_output)

print('Hexadecimal to Binary')
a_hexadecimal_number = h
binary_output = coden.hex_to_bin(a_hexadecimal_number)
print(h, '-->', binary_output)

print('Hexadecimal to Decimal')
a_hexadecimal_number = h
decimal_output = coden.hex_to_int(a_hexadecimal_number)
print(h, '-->', decimal_output)