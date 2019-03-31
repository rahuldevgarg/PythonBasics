def abc():
   #global a Not allowed multiple scopes of same variables
   #a = 'GLA'
   #a *= 2
    #global a
    def loc():
       a = 10
       print('I am local ', a)
    def noloc():
       nonlocal a
       a = 20
    def gbloc():
       global a
       a = 'GLA'
    a = 2
    loc()
    print(a)
    noloc()
    print(a)
    gbloc()
    print(a)
a=0
abc()
print(a)