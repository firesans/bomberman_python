We need to write a python program that simulates a basic version of Bomberman with different set of rules. 
You are responsible for destroying enemies and bursting the walls and winning the game :p 
 
As a template my code contains the following classes corresponding to respective objects in the game: 
1. Board 
2. Person 
3. Bomb 
4. Enemy
5. Main

Basic Controls - 

Play the game -> p
Move left -> a 
Move right -> d 
Move up -> w 
Move down -> s 
Drop bomb -> b 
Quit the game -> q


Game INSTRUCTIONS :

-> Written in python 2.7.12
-> To run the game: "python main.py"
-> Enter the character 'p' to play the game or 'q' to quit the game
-> Enemies start moving once the player(bomberman) starts moving
-> Bomberman has 3 lives ( he loses a life only when the enemy tries to kill him :( ),so play wisely. 
-> Game has 2 enemies and less than 10-12 bricks depending on random number generated.


Game Representations :

-> Bomberman is represented by [^^]
                                ][

-> Enemy is represented by     EEEE
                               EEEE

-> Bricks are represented by   %%%%
                               %%%%

-> Walls are represented by    ####
                               ####
