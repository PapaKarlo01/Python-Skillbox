task = input()
task = task.lstrip()
task += ' '
s = ''
for i in range(0, len(task)):
    if task[i] == ' ':
        s += task[i-1]
print(s)
input()
