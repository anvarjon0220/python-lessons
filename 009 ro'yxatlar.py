mevalar = ['olma', 'anor', 'anjir', "olxo'ri"]
narxlar = [100, 2000, 50000, 800000]
sonlar = ['bir', 'ikki', 3, 4, 5] #aralash ro'yxat
ismlar = [] #bo'sh ro'yxat

print(mevalar) #
print("Birinchi meva: ", mevalar[0]) #olma
print("Oxirgi meva: ", mevalar[-1]) #olxo'ri

#string metodlarni qo'llash
print("Birinchi meva: ", mevalar[0].upper()) #OLMA
print("Birinchi meva: ", mevalar[0].title()) #Olma

#arifmetik amallar
print(narxlar[2]+narxlar[3])

#element qo'shish, o'chirish, o'zgartirish
ismlar = ['Akbar', 'Muzaffar', 'Anvar', 'Sanjar']
print(ismlar)

#o'zgartirish
ismlar[0] = 'Anvar'
ismlar[2] = 'Akbar'
print(ismlar)

#qo'shish
ismlar.append('Sohib') #oxiriga qo'shish
print(ismlar)
ismlar.insert(0, 'Sharbat') #istalgan joyga qo'shish 
print(ismlar)
ismlar.insert(4, 'Shakar') #istalgan joyga qo'shish 
print(ismlar)
ismlar.insert(5, 'Samar') #istalgan joyga qo'shish 
print(ismlar)

#o'chirish
del ismlar[4] #indeksiga ko'ra o'chirish
print(ismlar)
ismlar.remove('Samar') #qiymatga ko'ra o'chirish
print(ismlar)

#.remove(qiymat) metodi ro'yxatda topilgan birinchi elementni o'chiradi

#elementni sug'urib (ajratib) olish
first_son = ismlar.pop(1)
print(first_son) #Anvar
print(ismlar)

#agar .pop() metodida indeks berilmasa, oxirgi element sug'urib olinadi