sodas = ["Fanta", "Vanilla Coke", "Gingerale"]
chips = ["Sunchips", "Pringles"]
candy = ["Snickers", "M&Ms", "Twix", "Swedish Fish"]

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry!".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
