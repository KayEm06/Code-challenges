class Number_Table():
    def __init__(self):
        self.symbol = input("Enter a maths symbol: ")
        self.number = int(input("Enter a number: "))

    def numbertable(self):

        line = f"{self.symbol} | {' '.join(str(i) for i in range(0, self.number+1))}"
        print(line)
        print("-" * len(line))

        for i in range(0, self.number+1):
            result = [eval(f"{j} {self.symbol} {i}") for j in range(0, self.number+1)]
            print(f"{i} | {' '.join(str(r) for r in result)}")

        
NumberTable = Number_Table()
NumberTable.numbertable()         

    