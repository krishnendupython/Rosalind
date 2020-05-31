a = input('input 1 = ') 
b = input('input 2 = ')
a1 = int(a)
b1 = int(b) 
total = 0
if a1<b1<10000:    
    if a1%2 == 0:
        for i in range (a1+1,b1,2):
            total += i
        
    else:
        for i in range (a1,b1,2):
            total += i
        total += a1 + b1
    print('Sum of odds between a and b = ',total)
elif a1>b1:
    print ('value of input 1 can not be greater than the value of input 2')
else:
    print ('input value >10000 not permitted')
    
