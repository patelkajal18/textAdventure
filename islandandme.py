#Start
print("You were having a great summer by yourself alone in the middle of the ocean on a boat. You take a little nap to take a break from your self pity session. When you wake up, you find yourself on an island and your boat is broken. You are really hungry but you also need shelter. Will you find food or shelter?")

#If incorrect answer is typed
def elsecase():
    print("That's not an option silly!")
    print("Start over by choosing food or shelter!")
    game()

#Game
def game():
    task1 = input()
    if task1 == "food":
        print("You decide to find some food. Type 'hunt' to look for animals or type 'fruit' to gather fruits")
        task2 = input()
        if task2 == "hunt":
            print("You run into a jaguar!!! Type 'run' to run away or type 'fight' to try scaring the jaguar")
            task3 = input()
            if task3 == "run":
                print("The jaguar is faster than you silly! You DIE!!")
            elif task3 == "fight":
                print("You can't fight a jaguar alone silly! You DIE!!")
            else:
                elsecase()
        elif task2 == "fruit":
            print("You can only find some red berries. Type 'eat' to eat them or type 'not' to not risk it")
            task3 = input()
            if task3 == "eat":
                print("Everyone knows not to eat red suspicious berries! You are POISONED and DIE!!")
            elif task3 == "not":
                print("Girl why you starving yourself? You STARVE and DIE!!")
            else:
                elsecase()
        else:
            elsecase()
    elif task1 == "shelter":
        print("You choose to build shelter. Type 'mountain' to climb the mountain or type 'beach' look around the beach?")
        task2 = input()
        if task2 == "mountain":
            print("While climbing up the mountain you run into a tiger! Type 'run' or 'hide' to try escaping the tiger")
            task3 = input()
            if task3 == "run":
                print("You can't out run a tiger silly! You DIE!!")
            elif task3 == "hide":
                print("You hide in a cave but you get caught because of a dead end. You DIE!!")
            else:
                elsecase()
        elif task2 == "beach":
            print("You find scraps of your broken boat. Type 'rebuild' to try rebuilding it or type 'house' to build a house out of the scraps")
            task3 = input()
            if task3 == "rebuild":
                print("YAY! You rebuild the boat and set off to go back home. Bon Voyage!")
            elif task3 == "house":
                print("You take too long to build the house and before you can finish, the cold night freezes you to DEATH!!")
            else:
                elsecase()
        else:
            elsecase()
    else:
        elsecase()

#Start/Restart game
print("start")
print("Type 'food' to find food or 'shelter' to go find shelter.")
game()
