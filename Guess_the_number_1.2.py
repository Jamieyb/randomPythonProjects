import random
def guesser(x):
    random_num = random.randint(1, x*10)
    chance = 10
    print(f"You have choosen level {x}\n")
    print(f"You have {chance} chances!")
    while chance > 0:
        guess = int(input(f"Guess a number between 1 and {x*10} : "))
        print("="*10)
        if guess > random_num:
            chance -= 1
            print('Too high, Try Lower!')
            print(f'{chance} chances left. Be mindful!\n')
            print("="*10)
        elif guess < random_num:
            chance -= 1
            print('Too Low, Try Higher!')
            print(f'{chance} chances left. Be mindful!\n')
            print("="*10)
        elif guess == random_num:
            print(f'YEAAYYY!!! {random_num} IS THE CORRECT NUMBER!\n')
        if chance==0:
            print("GAME OVER. You ran out of chances.")
            break

        

print("="*10)
lv = int(input("choose the level : \n"))
guesser(lv)