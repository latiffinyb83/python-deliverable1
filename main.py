print("Welcome to Gc mini golf!")
name = input("What is your name? ")

print('Hi '+name)
putts = input("Would you like to play 3 or 6 holes today? ")
print(putts)

# Total course par 9 if they chose 3
# Total course par 18 if they chose 6

if int(putts) == 3:
    hole = input("How many putts for hole 1? (par is 3): ")
    hole_two = input("How many putts for hole 2? (par is 3): ")
    hole_three = input("How many putts for hole 3? (par is 3): ")
    subtotal = int(hole) + int(hole_two) + int(hole_three)
    print(subtotal)
    if subtotal == 9:
        print("Good game, " + name)
        print('Your total par was 0')
    elif subtotal > 9:
        print("Nice try, " + name)
        print("Your total par was +" + str(subtotal - 9))
    else:
        print("Great job, " + name)
        print("Your total par was " + str(subtotal - 9))


elif int(putts) == 6:
    hole = input("How many putts for hole 1? (par is 3): ")
    hole_two = input("How many putts for hole 2? (par is 3): ")
    hole_three = input("How many putts for hole 3? (par is 3): ")
    hole_four = input("How many putts for hole 4? (par is 3): ")
    hole_five = input("How many putts for hole 5? (par is 3): ")
    hole_six = input("How many putts for hole 6? (par is 3): ")
    subtotal = int(hole) + int(hole_two) + int(hole_three) + int(hole_four) + int(hole_five) +int(hole_six)
    print(subtotal)
    if subtotal == 18:
        print("Good game, " + name)
        print('Your total par was 0')
    elif subtotal > 18:
        print("Nice try, " + name)
        print("Your total par was +" + str(subtotal - 18))
    else:
        print("Great job, " + name)
        print("your total par was " + str(subtotal -18))
