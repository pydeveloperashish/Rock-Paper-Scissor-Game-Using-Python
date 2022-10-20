"""
Course: Introduction to Python Programming
Student Name:
"""
#%% 
import random
from random import randint
from pprint import pprint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%


choices_list = ['rock', 'paper', 'scissors']

game_records = {
        "The_number_of_rounds" : [],
        "computer_choice" : [],
        "human_choice" : [],
        "no_of_Draws" : [],
        "no_of_Humans_wins" : [],
        "no_of_Computer_wins" : [],
                }

def HumanPlayer(human_choice):
    
        
    
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''
    return human_choice

# %%
def ComputerPlayer():
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    computer_choice = random.choice(choices_list)
    return computer_choice
    

# %%
Outcome = 0 
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''
    
    computer_choice = ChoiceOfComputerPlayer
    human_choice = ChoiceOfHumanPlayer
    
    
    
    if computer_choice == 'rock' and human_choice == 'paper':
        Outcome = 2
        print("Human Player Wins!!!")
    elif computer_choice == 'scissors' and human_choice == 'rock':
        Outcome = 2
        print("Human Player Wins!!!")
    elif computer_choice == 'paper' and human_choice == 'scissors':
        Outcome = 2
        print("Human Player Wins!!!")
        
    elif computer_choice == 'paper' and human_choice == 'rock':
        Outcome = 1
        print("Computer Player Wins!!!")
    elif computer_choice == 'scissors' and human_choice == 'paper':
        Outcome = 1
        print("Computer Player Wins!!!")
    elif computer_choice == 'rock' and human_choice == 'scissors':
        Outcome = 1
        print("Computer Player Wins!!!")
    
    elif computer_choice == human_choice:
        Outcome = 0
        print("Match is Draw!!! Try Again...")
    
    return Outcome

# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    
    computer_choice = ChoiceOfComputerPlayer
    human_choice = ChoiceOfHumanPlayer
    
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    print(f"Outcome : {Outcome}")
    print(f"Human choice is : {human_choice}")
    print(f"Computer choice is : {computer_choice}")

    
    

# %%
def UpdateGameRecord(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
    
    
    
    game_records["The_number_of_rounds"].append(Outcome)
    game_records["computer_choice"].append(ChoiceOfComputerPlayer)
    game_records["human_choice"].append(ChoiceOfHumanPlayer)
    
    if Outcome == 0:
        game_records["no_of_Draws"].append(Outcome)
    if Outcome == 1:
        game_records["no_of_Computer_wins"].append(Outcome)
    if Outcome == 2:
        game_records["no_of_Humans_wins"].append(Outcome)

    
# %%
def PrintGameRecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    
    pprint(f"The_number_of_rounds : {len(game_records.get('The_number_of_rounds'))}")
    pprint("computer_choices : " + str(game_records.get('computer_choice')))
    pprint("human_choices : " + str(game_records.get('human_choice')))
    pprint(f"no_of_Draws : {len(game_records.get('no_of_Draws'))}")
    pprint(f"no_of_Humans_wins : {len(game_records.get('no_of_Humans_wins'))}")
    pprint(f"no_of_Computer_wins : {len(game_records.get('no_of_Computer_wins'))}")
    


    
list_choices = ["r", "s", "p"]
# %% the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
    
    print("Lets Play!!!")
    print("rock, paper or scissors? (r or p or s)")
    print("or you want to see records of the game? (g)")
    print("or you want to quit the game? (q)")
    print()
    choice = input("Please make your choice: ")
    if choice == "q":
            print()
            print("---------GAME OVER!!!------------")
            
    while choice in list_choices:
        if choice == 'r':
            choice = "rock"
        elif choice == 's':
            choice = "scissors"
        elif choice == 'p':
            choice = "paper"
            
        
            
        
            
        human_choice = HumanPlayer(choice)
        computer_choice = ComputerPlayer()
        
        Outcome = Judge(ChoiceOfComputerPlayer = computer_choice, 
                    ChoiceOfHumanPlayer = human_choice)
    
        PrintOutcome(Outcome, ChoiceOfComputerPlayer = computer_choice, 
                 ChoiceOfHumanPlayer = human_choice)
        
        
    
        
        UpdateGameRecord(ChoiceOfComputerPlayer = computer_choice, 
                 ChoiceOfHumanPlayer = human_choice,
                 Outcome = Outcome)
        
        print()
        choice = input("Please make your choice: ")
        
        if choice == "g":
            print()
            print("-------------GAME RECORDS----------------")
            print()
            PrintGameRecord(game_records)
            print()
            choice = input("Please make your choice: ")
            
        if choice == "q":
            print()
            print("---------GAME OVER!!!------------") 
            
        elif choice not in list_choices:
            print("Please Enter a Valid Choice....")
            choice = input("Please make your choice: ")
        
        
      
        

    
        
        
       
           
        
# %% do not modify anything below
if __name__ == '__main__':
    print("Welcome to the Rock-Paper-Scissors Game!!!")
    PlayGame()
    
