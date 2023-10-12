stepsCount = int(input())
dx, dy = 0, 0
xTime, yTime = True, False
xFlag, yFlag = -1, -1
xMove, yMove = 1, 1
a, b = 0, 0
for i in range(0, stepsCount):
    if xTime: 
        dx += 1 * xFlag
        a += 1
        if a == xMove:
            xTime = False
            yTime = True
            xFlag *= -1
            xMove += 1
            a = 0
    else:
        dy += 1 * yFlag
        b += 1
        if b == yMove:
            yTime = False
            xTime = True
            yFlag *= -1
            yMove += 1
            b = 0
print(dx, dy)
input()
