import math
height=10
radius=5
flowRate=15
volTank = math.pi*math.pow(radius,2)*height

time = eval(input("Enter Time in Minutes : "))
volWater = flowRate*time

if volWater > volTank :
    print('OverFlow Condition')
    print('Volume Lost : ',volWater-volTank)
elif volWater==volTank :
    print('Tank is Full')
else:
    print("UnderFlow Condition")
    # ht=volWater/(math.pi*radius**2)
    ht = volWater // (math.pi * radius ** 2)
    hr = height - ht
    # r= 'Filled Height is {} and remaining height is {}'.format(ht,hr)
    # print(r)
    print('Filled Height is ', ht ,'and remaining height is ', hr )
