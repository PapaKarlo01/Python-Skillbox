task = input()
task = task[::-1]
task += '.'
count = 0
start = 0
for i in range(0, len(task)):
    if task[i] == '.':
        print(task[start:i][::-1])
        start = i + 1
input()
