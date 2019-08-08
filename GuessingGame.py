import random
########
# Simple guessing game program to test my knowledge of python (just recently started learning it)
# Grant Dennany, 6/18/19
#########
def GuessingGame():
    num = random.randint(1,100)
    userInput = []
    counter = 0
    print(f"------{num}-----\n\n")
    print("Welcome to the guessing game! Guess a number between 1 and 100 below:")
    userInput.append(int(input("")))

    if userInput[counter] == num:
      print(f'Congratulations! You guessed the number {num} correctly, and it only took you {counter + 1} attempt!')
      return

    while userInput[counter] > 100 or userInput[counter] < 1:
       print(f'{str(userInput[counter])} is not between 1 and 100! >:( Try again!')
       userInput.append(int(input("")))
       counter += 1

    if (abs(userInput[counter] - num)) <= 10:
       print("Warm! Try again: ")
       userInput.append(int(input("")))
    elif (abs(userInput[counter] - num)) > 10:
      print("Cold! Try again: ")
      userInput.append(int(input("")))
    counter += 1

    while userInput[counter] != num:
        if userInput[counter] > 100 or userInput[counter] < 1:
            print(f'{str(userInput[counter])} is not between 1 and 100! >:( Try again!')
            userInput.append(int(input("")))
        elif (userInput[counter] - num) == (userInput[counter - 1] - num):
            print("Thats the same number! Try again: ")
            userInput.append(int(input("")))
        elif (userInput[counter] - num) > (userInput[counter - 1] - num):
           print("Colder! Try again: ")
           userInput.append(int(input("")))
        elif (userInput[counter] - num) < (userInput[counter - 1] - num):
            print("Warmer! Try again: ")
            userInput.append(int(input("")))
        counter += 1

    if userInput[counter] == num:
        print(f'Congratulations! You guessed the number {num} correctly, and it only took you {counter + 1} attempts!')
        return
