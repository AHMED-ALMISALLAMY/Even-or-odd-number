def run():
    still_run = True
    while still_run:
        number = int(input("Enter a number to check if it 'even' or 'odd': "))
        if number % 2 == 0:
            print(f"{number} is even number.")
        else:
            print(f"{number} is odd number.")
        still_run = input("Do you want to continue 'y' or 'n': ").lower()

        if still_run == 'y':
            run()
        else:
            still_run = False
run()