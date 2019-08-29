"""
d = [2,4,5,6,7]
# print(*d) #with No Separator
print(*d, sep=';')  #Add your Custom separator
"""


def ret(a, b):
    print(a, type(a), sep=' ---> ')
    print(b, type(b), sep=' ---> ')

ret(2,3)
print("-----------------------")
ret((2), (2,3,4,5,6)) #redundant parenthesis in arg[0], touple in arg[1]
