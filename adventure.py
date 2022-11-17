import random
import time

weapons = ["sword", "shield", "axe", "bow", "staff"]
attackers_list = ["troll", "goblin", "dragon",
                  "wolf", "pirates", "wicked fairie"]
attacker = random.choice(attackers_list)
items = []


def pause_print(message_to_print):
    time.sleep(1.5)
    print(message_to_print)


def start_game():
    pause_print(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers.")
    pause_print(
        f"Rumor has it that a {attacker} is somewhere around here, "
        "and has been terrifying the nearby village.")
    pause_print("In front of you is a house.")
    pause_print("To your right is a dark cave.")
    pause_print(
        "In your hand you hold your trusty (but not very effective) dagger.\n")
    field(items)


def field(items):
    pause_print("Enter 1 to knock on the door of the house.")
    pause_print("Enter 2 to peer into the cave.")
    pause_print("What would you like to do?")
    destination = input("(Please enter 1 or 2.)")
    pause_print("\n")
    if destination == "1":
        # pause_print(f"tested okay {destination}")
        house(items)
    elif destination == "2":
        cave(items)
    else:
        pause_print("Invalid Input!!!\nPlease Try Again")
        field(items)


def house(items):
    pause_print("You approach the door of the house.")
    pause_print(
        f"You are about to knock when "
        "the door opens and out steps a {attacker}.")
    pause_print(f"Eep! This is the {attacker}'s house!")
    pause_print(f"The {attacker} attacks you!")
    if len(items) < 0:
        pause_print(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger.")

    fight_or_run = input("Would you like to (1) fight or (2) run away?")
    if fight_or_run == "1":
        fight(items)
    elif fight_or_run == "2":
        run()
    else:
        replay()


def replay():
    global items
    global attacker
    attacker = random.choice(attackers_list)
    items = []

    play_again = input("Would you like to play again? (y/n)")
    if play_again == "y":
        pause_print("Excellent! Restart_gaming the game ...")
        start_game()
    elif play_again == "n":
        pause_print("Thanks for playing! See you next time.")
        return
    else:
        replay()


def fight(items):
    # any(x in weapons for x in items)
    if len(items) != 0:
        pause_print(
            f"As the {attacker} moves to attack, you unsheath your new sword.")
        pause_print(
            "The Sword of Ogoroth shines brightly "
            "in your hand as you brace yourself for the attack.")
        pause_print(
            f"But the {attacker} "
            "takes one look at your shiny new toy and runs away!")
        pause_print(
            f"You have rid the town of the {attacker}. "
            "You are victorious!")
        replay()
    else:
        pause_print("You do your best...")
        pause_print(f"but your dagger is no match for the {attacker}.")
        pause_print("You have been defeated!")
        pause_print("GAME OVER!")
        replay()


def run():
    pause_print(
        "You run back into the field. Luckily,"
        "you don't seem to have been followed.")
    field()


def cave(items):
    if len(items) == 0:
        weapon = (random.choice(weapons))
        items.append(weapon)
        pause_print("You peer cautiously into the cave.")
        pause_print("It turns out to be only a very small cave.")
        pause_print("Your eye catches a glint of metal behind a rock.")
        pause_print(f"You have found the magical {weapon} of Ogoroth!")
        pause_print("You walk back out to the field.")
        field(items)
    else:
        pause_print("You peer cautiously into the cave.")
        pause_print(
            "You've been here before, and gotten all the good stuff."
            "It's just an empty cave now.")
        pause_print("You walk back out to the field.")
        field(items)


start_game()
