num = int(input())
boolFlag = False
for it in range(2, num):
    if num%it == 0:
        boolFlag = True
print("Not a Prime No" if boolFlag == True or num == 1 else "Prime No")
