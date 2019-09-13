n = int(input("Enter the amount : "))
if n % 100 != 0:
    print("Enter Denominations of 100, 500, 2000 ")
    exit()
new = n - 100
two = new // 2000
five = (new % 2000) // 500
hundred = ((new % 2000) % 500) // 100

print("2000 : {} 500 : {} 100 : {}".format(two, five, hundred + 1))
