guess_number = ["20","55","67"]
game_input = input().split()

for i in range(3):
    
    if game_input[i] in guess_number:
        print("You win 10rs..")
        break
    elif i == 2:
        print("Please Try Again...")