def pow_recursive(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        res = pow_recursive(a, n // 2)
        return res * res
    else:
        res = pow_recursive(a, n // 2)
        return res * res * a
a, b = int(input()), int(input())
print(pow_recursive(a, b))
input()
