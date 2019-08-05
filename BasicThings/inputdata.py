a=int(input('Enter the first value : '))
b=int(input('Enter Second Value : '))
c=a+b
"""
    in unpacked form
"""
print("Result is : ",c," of ",a," and ",b)
"""
    in type specific form
"""
print("Result is %d of %d and %d"%(c,a,b))
"""
    in format specifier mode
"""
h="Result is {} of {} and {}".format(c,a,b)
print(h)
h="{hg}Result is {2} of {1} and {1}{1}{1}".format(c,a,b,hg=[1,2,3,])
print(h)
h=f"Result is {c} of {a} and {b}"
print(h)