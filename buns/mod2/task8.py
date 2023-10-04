task = input()
comma = task.find(',')
text = task[0:comma]
count = 0
letter = task[comma + 1::]
for i in range(0, len(text)):
    if text[i] == letter:
        count += 1
    else:
        break
print(count)
input()
