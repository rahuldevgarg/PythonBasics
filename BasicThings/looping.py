# n = '123456789'
# n = range(15)
# n = range(1,15,2) #range(start,stop,step)
# for i in n:
#     print(i)
n = int(input('Enter the Number : '))
s = 0
# for i in range(n+1):
#     s+=i
for i in range(1,n):
    s = s + i
    # i = 10
print(s)
