start_year = int(input("Enter the first year: "))
end_year = int(input("Enter the second year:"))

def repeated_digit(start_year, end_year):
    count = 0
    list_of_years = []
    for i in range(start_year, end_year+1):
        if any(str(i).count(str(j)) > 1 for j in range(10)):
            list_of_years.append(i)
    return list_of_years    

print(f"In the range {start_year} to {end_year} the years that had repeated digits are: ", end="")
for i in repeated_digit(start_year, end_year):
    print(i, end = " ")