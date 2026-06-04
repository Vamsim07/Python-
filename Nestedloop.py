row = int(input("Enter row Number :"))
column = int(input("Enter column :"))
symbol = input("Enter symble :")

for i in range(row):
    for j in range(column):
        print(symbol, end="")
    print()
