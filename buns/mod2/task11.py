task = input()
flag = False
for i in range(0, len(task), 2):
    for j in range(i + 2, len(task), 2):
        if task[i] == task[j]:
            flag = True
            break
print(flag)
input()
