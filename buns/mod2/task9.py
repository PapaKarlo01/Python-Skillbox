task = input()
vowels = 'аАеЕиИоОуУыЫэЭюЮяЯёЁ'
unvowels = 'БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщЪъЬь'
countvowels = 0
countunvowels = 0
for i in range(0, len(task)):
    if task[i] in vowels:
        countvowels += 1
    elif task[i] in unvowels:
        countunvowels += 1
print(countvowels, countunvowels)
input()
        
