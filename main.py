
h, w = input().split(' ')
h = int(h)  
w = int(w)  

n = int(input())  

a = list(input().split(' '))  

cal = 2.54  #

dobretel = []  
for i in a:
    o = int(i)  

    
    htel = ((o ** 2 + 9 ** 2) / (16 ** 2 + 9 ** 2)) ** 0.5  
    wtel = (16 / 9) * htel  

    htel *= cal
    wtel *= cal

    if h >= htel and w >= wtel:
        dobretel.append(o)


if dobretel:
    
    print(dobretel[n - 1])
else:
   
    print("NIE")
