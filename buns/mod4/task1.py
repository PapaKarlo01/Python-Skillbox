taskList = input().split(' ')
flag1, flag2 = 0, 0
for i in range(0, len(taskList)):
    for j in range(i + 1, len(taskList)):
        if taskList[i] == taskList[j]:
            flag1 += 1
        else:
            flag2 += 1
if flag1 == 0 and flag2 != 0:
    print('Все числа разные')
elif flag1 != 0 and flag2 == 0:
    print('Все числа равны')
else:
    print('Есть равные и неравные числа')


    
