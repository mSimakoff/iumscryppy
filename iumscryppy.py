import math
import os
import datetime  # импортируем библиотеку датывремени
now = datetime.datetime.now()  # получаем сегоднюшнюю датувремя, это наш уникальный ключ
time = int(now.strftime("%H%M%S"))  # форматируем нашу датувремя в корректный формат и делаем числом, для этого int()
key = time + 1108  # просто нравится это число, поэтому прибавляем его

key //= 10000

if (int(now.strftime("%M"))) <= 20 and (int(now.strftime("%M"))) >= 2:
    key = int(now.strftime("%M"))

print(key)  # пока все, просто выводим наш унникальный ключ

text = input('')
s1 = ""
ftxt = ""
for i in text:
    if ord(i) + key > ord("я"):  # ord/chr - работаем с таблицей ASCII
        s1 += chr(ord(i) + key - 32)
    else:
        s1 += chr(ord(i) + key)
print(s1)
lfh = key
#output = open('key.txt','w')
#output.write('Key is:', lfh)
#KOD

final = ''
k = 0
for i in s1:

    if (ord(i) >= 1040) and (ord(i) <= 1103):
        if (k % 2) > 0:
            k += 3
        else:
            k += 1
        # какая то последовательность
        # докидывать нули через длину строки
        n = ""
        ll = k
        while ll > 0:
            y = str(ll % 2)
            n = y + n
            ll = int(ll / 2)
        i = str(n)
        while len(i) == 5:
            i = '0' + i
        final += i
        k += 1
    elif (ord(i) >= 32) and (ord(i) <= 63):  # пробелы
        l = '00000'
        final += l
    elif (ord(i) == 33):  # Знак восклицания
        l = '001'
        final += l
    elif (ord(i) == 63):  # Знак вопроса
        l = '010'
        final += l
    elif (ord(i) == 44):  # Запятая
        l = '011'
        final += l
print(final)


s1 = final

k = len(s1)
print(s1)

#RLE

vvod = s1  #  input()
if len(vvod) > 1:
    count = 1
    prev = ''
    lst = []
    for i in vvod:
        if i != prev:
            if prev:
                entry = ''
                entry = str(count) + prev
                lst.append(entry)
            count = 1
            prev = i
        else:
                count += 1
    else:
        entry = str(count) + i
        lst.append(entry)
    edinici = ''.join(lst)
    x = ''
    for i in edinici:
        if i != '2': #поменять в зависимости от фразы
            x = x + i
    print("RLE is ",x)
else:
    print("RLE is ",vvod)

k /= len(x)
print('Compression ratio ', k)
