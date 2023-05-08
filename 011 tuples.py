#tuples - o'zgarmas ro'yxat, u () oddiy qavslar ichida yoziladi

tomonlar = (20, 30, 55.2)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys)

#agar tuplega o'zgartirmoqchi bo'lsak, avval uni list ga aylantirib olamiz
toys = list(toys)
#'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
#qaytadan tuple ga aylantiramiz
toys = tuple(toys)
print(toys)