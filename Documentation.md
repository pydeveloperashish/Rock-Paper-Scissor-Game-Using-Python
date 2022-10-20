### Introduction to the Game:
This game is a simple Rock-Paper-Scissor Game built using Python

### Requirements specifications of the assignment
- Python version >= 3.7.0
- pprint library
- random library

### Application and Implementation

- There are two players: one player is a human user represented by the function
  “HumanPlayer”, and the other player is the function “ComputerPlayer”.


- The function HumanPlayer will parse user input from the computer keyboard, and it should
  be able to handle random input string from the human user. The human user may also
  choose to print the record of the game or quit.
  This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord


- The function “ComputerPlayer” will use a random strategy: select rock/paper/scissors
  randomly. You will need to import the package random to use the function randint. 
  ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer


- The outcome of a game will be determined by the function “Judge” and printed to the
  console. The game will be played many rounds until the human user wants to quit.

- The "PrintOutcome" functions print Outcome, Choices and Players to the console window
        the message should be human readable


- A list “RecordOfGame” will be used to keep a record of players' choices and outcomes. It
  will be updated after two players have made the choices at each round.


- The "PrintGameRecord" function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.


### Output Screenshots

