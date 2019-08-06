# r = (input('Enter a Char : '))
# if 65 <= ord(r) <= 90:
#     print("Uppercase Alphabet")
# elif 97 <= ord(r) <= 122:
#     print("Lowecase Alphabet")
# elif 48 <= ord(r) <= 57:
#     print("Number")
# else:
#     print("Special Char")
"""--------------------------------------------------------"""
# r = (input('Enter a Char : '))
# if 'A' <= r <= 'Z':
#     print("Uppercase Alphabet")
# elif 'a' <= r <= 'z':
#     print("Lowecase Alphabet")
# elif '0' <= r <= '9':
#     print("Number")
# else:
#     print("Special Char")
"""------------------------------------------------------"""
r = (input('Enter a Char : '))
if r >= 'A' and  r <= 'Z':
    print("Uppercase Alphabet")
elif  r >= 'a' and  r <= 'z':
    print("Lowecase Alphabet")
elif  r >= '1' and  r <= '9':
    print("Number")
else:
    print("Special Char")