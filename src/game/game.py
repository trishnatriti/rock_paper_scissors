""""
rock = 1
paper = 2
scissor = 3
"""

import random

class Game:
    def __init__ (self, name):
        self.name = name
        
    def game_rps (self, user:int):
        sys = random.randint(1,3)
        if user==sys:
            result = "draw"
            print((f"{user}\t{sys}"))
            
        elif user==1 and sys==2:
            result = "User Wins😎"
                    
        elif user==1 and sys==3:
            result = "User Wins🫡"
        
        elif user==2 and sys==1:
            result="User wins🥳"
            
        elif user==2 and sys==3:
            result="System wins🕺"
        
        elif user==3 and sys==1:
            result = "System Wins💃"
            
        elif user==3 and sys==2:
            result="User wins😀"
        
        else:
            print("Incorrect Input")
                
        game_df = {1:"Rock", 2:"Paper", 3:"Scissor"}
            
        print(f"{result}\n{self.name} selected {(game_df[user])}\nsystem selected {(game_df[sys])}")
                  
player = Game("Trishna")
player.game_rps(1)