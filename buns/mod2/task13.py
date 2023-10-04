task = input()
odd = 0
even = 0
for i in range(0, len(task)):
    if i % 2 == 0:
        odd += int(task[i])
    else:
        even += int(task[i])


if (even * 3 + odd) % 10 == 0:
    print('yes')
else:
    print('no')

input()
