def perimeter(a):
    return 4 * a

def area(a):
    return a * a

def diagonal(a):
    return a * (2 ** 0.5)

side = float(input())
perimeter_result = "%.2f" % perimeter(side)
area_result = "%.2f" % area(side)
diagonal_result = "%.2f" % diagonal(side)
print(perimeter_result + ", " + area_result + ", " + diagonal_result)

input()