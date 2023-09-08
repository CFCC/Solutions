def calculate_price_per_dozen(num_eggs: int):
    if num_eggs < 48:
        return 0.5
    elif 48 <= num_eggs < 72:
        return 0.45
    elif 72 <= num_eggs < 132:
        return 0.4
    else:
        return 0.35


choice = input("Please enter 'c' for a calculator or 't' for a table: ")
if choice[0:1].lower() == "c":
    num_eggs = input("Please enter the number of eggs: ")
    price_per_dozen = calculate_price_per_dozen(int(num_eggs))
    print("Your cost is $" + str(price_per_dozen) + " per dozen or $" + str(price_per_dozen / 12) + " per egg.")
    print("Your total bill comes to $" + str(price_per_dozen * int(num_eggs) / 12))
elif choice[0:1].lower() == "t":
    for num_eggs in range(1, 121):
        print(str(num_eggs) + " " + str(calculate_price_per_dozen(num_eggs) * num_eggs / 12))
else:
    print("I'm sorry, that's not an option.")
