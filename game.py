guess_number = ["20","55","67"]
game_input = input("Enter 3 Lucky Number: ").split()

for i in guess_number:
    if (game_input[0] in guess_number) or (game_input[1] in guess_number) or (game_input[2] in guess_number) :
        if i == game_input[0]:
            print("You Win 10rs..")
            print()
        elif i == game_input[1]:
            print("You Win 8rs..")
            print()
        elif i == game_input[2]:
            print("You Win 5rs...")
            print()
    else:
        print("Please Try Again...")
        break