#import the build in function from the python libraries
import random
import os 
#define the main module
def main():
    #call the functions to the main module
    Welcome_message()
    menu()
#function for welcome message
def Welcome_message():
    print ("""\n    Welcome to my Rock, Paper, Scissors game program.
    This is my final project for COP1000
    Name: Edgar Meruvia Garron
    Professor: Sherry Cox""")
#main menu function
def menu():
    #loop the main program so that it will keep running until the user says otherwise.
    endProgram = 0
    while endProgram != 4:
        endProgram = int(input("""
            Main Menu
         
    1. See the rules of the game.
    2. Play against the computer.
    3. Play a two player game.
    4. Quit the game.

    Select your option: """))
        print ("")
        #if statements to determine what function is going to be called according to the user.
        if endProgram == 1:
            rules()
        elif endProgram == 2:
            comp()
        elif endProgram == 3:
            pvp()
        elif endProgram == 4:
            print ("    Thanks for playing, Bye. \n")
        #when the user enters something that is not from 1-4 it will tell the user to enter a proper value.
        else:
            print("    That is not a valid option, please enter a given option (1-4).")
#rules function, it will show the user the functions.
def rules():
    #triple quotation marks to use only 1 print statement.
    print ("""    These are the rules of the game:

    -Paper Covers Rock
    -Rock Smashes Scissors
    -Scissor Cut Paper
    """)
#weapon menu function.
def Weapon_menu():
    #show the weapon menu
    print ("""
    Weapon Menu:
    1. Rocks.
    2. Paper.
    3. Scissor.
    4. Go back to main menu.
    """)
    #Ask the user for his weapon.
    weapon = int(input("    Select your weapon: "))
    if weapon == 1:
        weapon == "Rocks"
    elif weapon == 2:
        weapon == "Paper"
    elif weapon == 3:
        weapon == "Scissors"
    elif weapon == 4:
        menu()
    else:
        print ("Please choose 1 of the 4 options.")
        weapon = int(input(''))
    return weapon
#cls function
def cls():
    #this function uses the os import from the library.  It gives the option to the user to clear the screen after he is done playing.
    clear = input("Press (yes/y) if you want to clear the screen:")
    if clear.lower() == "yes" or clear == "y":
        os.system('CLS')
    else:
        menu()
 #function pvcp
def comp():
    #ask the user how many rounds he wants to play
    total_turns = int(input("    Enter how many rounds do you want to play: "))
    turns = 0
    Player_won = 0
    Comp_won = 0
    #create a loop that will run the number of rounds the user entered.
    while(turns < total_turns):
        #randint uses the random import from library. It lets the  computer to generate a random number with the set limits.
        computer_choice = random.randint(1,3)
        player_choice = Weapon_menu()
        #show the weapon choosen by the computer and by the player.
        print ("    You choose: ", player_choice, "The computer choose: ", computer_choice)
        if (player_choice == 1 and computer_choice == 2):
            print ("    You lose. Paper beats Rocks.\n")
            Comp_won += 1
        elif (player_choice == 1 and computer_choice == 3):
            print ("    You win. Rocks beats Scissors\n")
            Player_won += 1
        elif (player_choice == 2 and computer_choice == 1):
            print ("    You win. Paper beats Rocks\n")
            Player_won += 1
        elif (player_choice == 2 and computer_choice == 3):
            print ("    You lose. Scissors beats Paper.\n")
            Comp_won += 1
        elif (player_choice == 3 and computer_choice == 1):
            print ("    You lose. Rocks beats Scissors.\n")
            Comp_won += 1
        elif (player_choice == 3 and computer_choice == 2):
            print ("    You win. Scissors beats Rocks\n")
            Player_won += 1
        elif (player_choice == computer_choice):
            print ("    It's a tie.\n")
        print ("""              The Scores are: 
        Player""", Player_won, "------- Computer", Comp_won)
        turns +=1
    #show if the computer or player won the round and with how many points.
    if Player_won > Comp_won:
        print ("    You won by", Player_won - Comp_won, "points in", total_turns, "rounds.\n")
    elif Player_won == Comp_won:
        print ("    You are tied with the computer in", total_turns, "rounds.\n")
    else:
         print("\tYou lost by", Comp_won - Player_won, "points in", total_turns, "rounds.\n")
    #call the cls function to clear screen
    cls()
#function pvp
def pvp():
    rounds = 0
    #ask the user how many rounds they want to play.
    total_rounds = int(input("    Enter how many rounds you want to play: "))
    player1_won = 0
    player2_won = 0
    #this will let the computer run the program the set amount of times the user selected.
    while (rounds < total_rounds):
        #call weapon menu functions
        print ("""
        Player 1 : """)
        player1_Choice = Weapon_menu()
        print ("""
        Player 2 : """)
        player2_Choice = Weapon_menu()
        print ("")
        #show what player won
        if (player1_Choice== 1 and player2_Choice==2):
            print("    Player 2 wins. Paper beats Rocks.")
            player2_won += 1
        elif (player1_Choice ==2 and player2_Choice ==1 ):
            print("    Player 1 wins. Paper beats Rocks.")
            player1_won += 1
        elif (player1_Choice ==1 and player2_Choice ==3 ):
            print("    Player 1 wins. Rocks beats Sccissors.")
            player1_won += 1
        elif (player1_Choice ==3 and player2_Choice ==1 ):
            print("    Player 2 wins. Rocks beats Sccissors.")
            player2_won += 1
        elif (player1_Choice ==3 and player2_Choice ==2 ):
            print("    Player 1 wins. Scissors beats Paper.")
            player1_won += 1
        elif (player1_Choice ==2 and player2_Choice ==3 ):
            print("    Player 2 wins. Scissors beats Paper.")
            player2_won += 1
        else:
           print("    Player 1 and Player 2 tied.")
        #display the scores of each player
        print ("""
                  The Scores are: 
        Player 1 -""", player1_won, "------- Player 2 -", player2_won)
        print ("")                
        rounds += 1
    #display which player has won and in how many rounds.
    if (player1_won > player2_won):
        print ("\tPlayer 1 won by", player1_won, "points in", total_rounds, "rounds. \n")
    elif (player2_won > player1_won):
        print ("\tPlayer 2 won by", player2_won, "points in", total_rounds, "rounds. \n")
    elif (player1_won == player2_won):
        print ("\tPlayer 1 and Player 2 tied with", player1_won, "points in", total_rounds, "rounds. \n")
    #call cls function
    cls()
        
main()