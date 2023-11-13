letters = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрс'
           'туфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
file_name = input()
f = open(file_name, 'r', encoding='utf-8')
all_letters = set()
all_symbols = ''
for line in f:
    for letter in line:
        if letter in letters:
            all_letters.add(letter)
        all_symbols += letter

f.close()


letter_dict = {i: 0 for i in all_letters}


for letter in all_symbols:
    if letter in letter_dict:
        letter_dict[letter] += 1

k = open('output.txt', 'w', encoding='utf-8')

sorted_dict = dict(sorted(letter_dict.items(), key= lambda x:x[1]))
for result in sorted_dict.items():
    k.write(str(result) + '\n')

k.close()




