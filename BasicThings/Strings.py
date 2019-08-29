"""Strings.py : Continuous set of charracters represented within any qoutation is a string, wheather it is ' ' or " ".
 Python does not support a char type"""
# String is immutable
h = 'gdsghdsfghcdghsdfghdfghkfdtyfbjbbjhdshjgscgfd'
j = ''
num = len(h)
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            continue
        else:
            j += h[i]
else:
    print(None)
print(j)
