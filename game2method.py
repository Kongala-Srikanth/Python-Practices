guess_lucky_number = ["20", "35","66"]
guess_fisrt_number = input("Enter First Lucky Number: ")

if guess_fisrt_number in guess_lucky_number:
    print("You won reward")
    print()
else:
    print("First number worng. Try another two numbers.")
    second_chance =input("Enter Two Lucky Number: ").split()
    if (second_chance[0] in guess_lucky_number) or (second_chance[1] in guess_lucky_number):
        print("You Won Reward...")
    else:
        print("You Loss")
        print("Please Try Again...")
print("__________________________________________________________________________")