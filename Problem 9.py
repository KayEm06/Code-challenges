def IsHappy(num):
    total = 0
    while num != 1:
        total = 0
        for n in str(num):
            squared = int(n) * int(n)
            total += squared
        num = total
        if num == 4:
            return False
    return True

def FirstEightHappyNumbers(num):
    lst = []
    while len(lst) < 8:
        if IsHappy(num) == True:
            lst.append(num)
        num += 1
    print(lst)

FirstEightHappyNumbers(1)