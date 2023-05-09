car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

# Bu 3 ta lug'atdan ro'yxt hosil qilamiz:
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")
    
print(cars[0]['model'])

# for sikli yordamida bo'sh lug'atlar ro'yxatini yaratish mumkin:
malibus = []
for n in range(10):
    new_car = { # har bir avto uchun lug'at
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narx':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)

for malibu in malibus:
    print(malibu)
    
for m in malibus[:3]: # dastlabki 3 tasi
    m['rang']='qizil'

for m in malibus[3:6]:
    m['rang']='qora'
    
for m in malibus[6:]:
    m['rang']='qora'
    m['korobka']='mexanika'
    
for m in malibus:
    if m['korobka']=='avto':
        m['narx']=40000
    else:
        m['narx']=35000
        
for malibu in malibus:
    print(malibu.values())
    
# nested list/dict

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

# Pythondagi print() funktsiyasi har bir matndan so'ng yangi qator tashlaydi.
# Buning oldini olish uchun quyidagi usuldan foydalanish mumkin: print(string, end = '')
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')


hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())





