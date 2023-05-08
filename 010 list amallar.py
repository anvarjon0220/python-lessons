ismlar = ['Sharbat', 'Anvar', 'Muzaffar', 'Akbar', 'Sanjar']
ismlar.sort()
print(ismlar)

#Bosh harflar kichik harflardan oldin keladi
ismlar2 = ['sharbat', 'anvar', 'Muzaffar', 'akbar', 'Sanjar']
ismlar2.sort()
print(ismlar2)

#teskari tartiblash
ismlar = ['Sharbat', 'Anvar', 'Muzaffar', 'Akbar', 'Sanjar']
ismlar.sort(reverse=True)
print(ismlar)

#sorted() funksiyasi asl ro'yxatga ta'sir qilmasdan tartiblaydi
print(sorted(ismlar))
print(ismlar)

#sorted teskari tartiblash
print(sorted(ismlar, reverse=True))
print(ismlar)

#ro'yxatni aylantirish
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
fruits.reverse()
print(fruits)

#ro'yxat uzunligi
print(f"elementlar soni: {len(fruits)}")

#range(start, stop, step) funksiyasi
sonlar = list(range(0, 100, 15))
print(sonlar)

#max, min, sum qiymatlar
narxlar = [12, 3, 800, 345, 42, 231]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon: ", arzon, \
      ". Eng qimmati: ", qimmat, \
      ". Jami: ", jami)

#ro'yxatni kesish
cars = ['volvo', 'bmw', 'toyota', 'tesla', 'audi', 'mersedes', 'ford']
my_cars = cars[0:3]
print(my_cars)
print(cars)

#ro'yxatdan nusxa olish
sonlar = list(range(1,6))
sonlar2 = sonlar
sonlar2.append(6)
sonlar2.append(7)
print(sonlar)
print(sonlar2)

#natija biz kutgandek emas, sababi manzil bitta
sonlar = list(range(1,11))
sonlar2 = sonlar[:] #[:] ro'yxatni to'liq nusxalaydi
sonlar2.append(11)
print(sonlar)
print(sonlar2)








