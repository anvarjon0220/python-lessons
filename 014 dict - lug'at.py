car = {
    'make':'GM',
    'model':'Malibu',
    'color':'Black',
    'gear':'automatic',
    'year':2023
    }

#print(narx)
narx = car.get('narx','Bunday kalit mavjud emas')
print(narx)

car['narx'] = 40000
print(car)
del car['color'] #kalit-qiymatni o'chirish
print(car)

print(car.items()) # lug'at elementlarini ko'rish

for kalit, qiymat in car.items():
    print(f'kalit:{kalit}')
    print(f'qiymat:{qiymat}')
    
# .keys() metodi
# agar lug'atdagi kalit so'zlarni topish talab qilinsa shu metod ishlatiladi

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())   # kalitlar

print(mahsulotlar.values()) # qiymatlarni  chop etish

# for siklidan foydalanib kalit yoki qiymatlarni olishimiz mumkin
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.values(): # .values() ni yozmasak, keys() ma'lumotlari chiqadi
    print(mahsulot)

# ro'yxatga mos qiymatlarni olish
bozorlik = ['anor', 'uzum', 'non', 'baliq']
for m in mahsulotlar:
    if m in bozorlik:
        print(f"{m.title()} {mahsulotlar[m]} so'm")

# lug'atda yo'q bo'lgan ro'yxat elementlarini qaytarish
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Kechirasiz, bizda {buyum} yo'q")
    
# ro'yxat elementlarini tartib bilan chiqarish
print("Do'konimizdagi mahsulotlar:")    
for m in sorted(mahsulotlar):
    print(m.title())