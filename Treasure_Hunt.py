def main():
    print("Welcome to the Adventure Game!")
    print("You find yourself standing in front of four mysterious doors.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Open the left door")
        print("2. Open the right door")
        print("3. Open the door in front of you")
        print("4. Open the door behind you")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print("\nYou open the left door and find a treasure chest!")
            print("Congratulations! You win!")
            break
        elif choice == '2':
            print("\nYou open the right door and are attacked by a monster!")
            print("Game Over!")
            break
        elif choice == '3':
            print("\nYou open the door in front of you and find a key.")
            print("You can use this key to unlock one of the other doors.")
            print("1. Use the key to open the left door")
            print("2. Use the key to open the right door")
            sub_choice = input("Enter your choice (1/2): ")
            if sub_choice == '1':
                print("\nYou use the key to open the left door and find a hidden passage.")
                print("You discover a secret room with valuable artifacts!")
                print("Congratulations! You win!")
                break
            elif sub_choice == '2':
                print("\nYou use the key to open the right door and are engulfed by darkness.")
                print("You are trapped in a maze. You wander for hours but find no way out.")
                print("Game Over!")
                break
            else:
                print("\nInvalid choice.")
        elif choice == '4':
            print("\nYou open the door behind you and find a portal to another dimension!")
            print("You step through the portal and find yourself in a magical realm.")
            print("You embark on a new adventure!")
            print("Congratulations! You win!")
            break

        elif choice=='5':
            print("\nGood Bye! Thanks for playing")
            break
        else:
            print("\ninvalid choice.please enter 1 or 2 or 3 or 4 or 5")
main()
        
        
        
 


