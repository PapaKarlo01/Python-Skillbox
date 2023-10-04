task = input()
count1 = 0
count0 = 0
for i in range(0, len(task)):
    if task[i] == '1':
        count1 += 1
    else:
        count0 += 1
if count1 == count0:
    print('yes')
else:
    print('no')
input()
