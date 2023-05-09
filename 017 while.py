son = 1
while son<=5:
    print(son, end=' ')
    son+=1
print()    
# while va input()
x = ''
while x!='stop':
    print('Istalgan sonning kvadratini qaytaruvchi dastur:')
    print('To\'xtatish uchun stop deb yozing')
    x=input('x=')
    if x!='stop':
        print(float(x)**2)
        
# flag - ishora
print('Istalgan sonning kvadratini qaytaruvchi dastur:')
print('To\'xtatish uchun stop deb yozing')
ishora = True
while ishora:
    x=input("x=")
    if x=='stop':
        ishora = False
    else:
        print(float(x)**2)
        
# break - siklni to'xtatish
print('Istalgan sonning kvadratini qaytaruvchi dastur:')
print('To\'xtatish uchun stop deb yozing')
while True:
    x=input("x=")
    if x=='stop':
        break
    else:
        print(float(x)**2)
        
# continue - tashlab o'tish, davom etish
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    else:
        print(f"{son**2}")

        
        
        