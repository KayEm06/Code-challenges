def kaprekar(num):
    squared = str(num * num)
    to_half = len(squared) // 2
    left_squared = squared[:to_half]
    right_squared = squared[to_half:]

    if int(left_squared) + int(right_squared) == num:
        return "Kaprekar number"
    else:
        return "Not a Kaprekar number"

num = int(input("Enter a number: "))
print(kaprekar(num))
