a = 10
b = 3
# c = False
# if a > b:
#     print('a is greater')
#     c = True
# else:
#     print('b is greater')
# print(c)
c = False if a < b else True
print(c)
print('a is equal to b ' if a==b else 'a is lower than b ' if a < b \
    else 'a is greater')
