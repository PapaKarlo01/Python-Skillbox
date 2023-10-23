word = input()
count = 0
for letter in set(word):
    count += word.count(letter) // 2
if count == (len(word) - len(word) % 2) // 2:
    print('палиндром')
else:
    print('не палиндром')
