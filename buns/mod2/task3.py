def find_middle_number(string_numbers):
    string_numbers = string_numbers.replace(' ', 'a')
    a = int(string_numbers[0 : string_numbers.find('a')])
    b = int(string_numbers[string_numbers.find('a') + 1 : string_numbers.rfind('a')])
    c = int(string_numbers[string_numbers.rfind('a') + 1::])
    if (b <= a <= c) or (c <= a <= b):
        print(a)
    elif (a <= b <= c) or (c <= b <= a):
        print(b)
    else:
        print(c)

string_numbers = input()
find_middle_number(string_numbers)
input()
                       
    
