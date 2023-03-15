import random
highest = int(input("enter the highest Number: "))
lowest = int(input("enter the lowest Number: "))
answer = random.randint(lowest, highest)
print(answer)
print("please guess number between {} to {}".format(lowest, highest))
guess = 0
# while guess == 00:
#     print("quit")
#     break
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("quit")
        break
    if guess == answer:
        print("you guessed it right")
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")





    print('guess higher')
    guess=int(input())
    if guess == answer:
        print("you guessed it")
    else:
        print("you did not guess correctly")


