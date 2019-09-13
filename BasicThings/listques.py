# in exam
# remove Duplicates in List
f = eval(input("Enter a List : "))
h = []
for i in f:
    if i not in h:
        h.append(i)
print(h)
