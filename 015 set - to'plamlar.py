# to'plam figurali {} qavslar ichida yoziladi
sonlar = {1,2,3,4,5}
ismlar = {'Alijon','Valijon','Boqijon'}
print(sonlar)
print(ismlar)

# To'plam bir xil elementlarni saqlamaydi
sonlar = {1,2,3,3,4,4,5,6,5,4,4,7}
print(sonlar)

# bo'sh to'plam yaratish uchun set()
a = set()

# to'plam elementlarida indeks bo'lmaydi, ya'ni tartiblanmaydi
#print(sonlar[0])

# to'plamni ro'yxatga o'tkazish
ismlar = list(ismlar)

# to'plamga element qo'shish
# .add() - bitta element qo'shish
mevalar = {'anjir', 'olma', 'uzum'}
mevalar.add('banan')
print(mevalar)

# .uppdate() - bir nechta element qo'shish
mevalar.update(['anor', 'qovun'])
print(mevalar)

# .update() ga parametr sifatida ro'yxat yoki lug'at uzatish mumkin.

# to'plamdan element o'chirish
# .discard()
mevalar.discard('anjir')
print(mevalar)

# .remove()
mevalar.remove('banan')
print(mevalar)

# agar element to'plamda mavjud bo'lmasa, .remove() metodi xato qaytaradi, .discard() esa yo'q

# .pop() metodi to'plamdan tasodifiy elementni sug'urib oladi, chunki to'plamda indeks yo'q
sonlar = {10,42,13,14,35,16,7}
son = sonlar.pop()
print(son)
print(sonlar)

# to'plamlarni birlashtirish: | yoki .union()
A = {1,2,3,4}
B = {3,4,5,6}
C = A|B
print(C)

D = A.union(B)
print(D)

# ikki to'plamnin kesishmasi (umumiy elementlari) ni topish: & yoki .intersection()
print(A&B)
print(A.intersection(B))

# to'plamlar ayirmasi: A-b yoki A.difference(B)
print(A-B)
print(A.difference(B))

# simmetric farq - bir aqtda ikkala to'plamga kirmaydigan elementlar
print(A^B)
print(A.symmetric_difference(B))







