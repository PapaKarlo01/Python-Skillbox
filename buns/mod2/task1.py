def find_Reminder(a, b):
    return a % b

example = input()
first_number = float(example[0:example.find(',')])
second_number = float(example[example.find(' ') + 1::])
print(find_Reminder(first_number, second_number))

input()

