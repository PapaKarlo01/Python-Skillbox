task = input()
i = task[0]
n = task[2::]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[(alphabet.find(i) + int(n)) % 26])
input()
