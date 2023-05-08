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

print(car.items())

for kalit, qiymat in car.items():
    print(f'kalit:{kalit}')
    print(f'qiymat:{qiymat}')
    
