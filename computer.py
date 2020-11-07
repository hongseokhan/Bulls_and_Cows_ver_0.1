import random
from player import Player
from gameinterface import Gameinterface

class Computer(Player):

    def __init__(self):
        super().__init__()
    @property
    def num_list(self):
        return self._num_list
    
    @num_list.setter
    def num_list(self,num_list):
        self._num_list = num_list
        
    def _random_generator(self):
        self._num_list = [str(x) for x in random.sample(range(1,10),4)]
        
    
    def input_algorithm(self,attacker,defender):
        #step1
        game=Gameinterface()
        a = ['1','2']
        b = ['3','4']
        c = ['5','6']
        d = ['7','8']
        e = ['9','0']
        attacker.num_list = a.append(b)
        game.strikes_and_balls_counter(attacker,defender)
        game.show_result(attacker)
        sb_total = attacker.strikes + attacker.balls
        if sb_total == 0:
            attacker.num_list = c.append(d)
            game.strikes_and_balls_counter(attacker,defender)
            game.show_result(attacker)
            if sb_total == 2:
                attacker.num_list = c.append(e)
                game.strikes_and_balls_counter(attacker,defender)
                game.show_result(attacker)
                if sb_total == 3:
                    attacker.num_list =[5,7,9,0]
                    game.strikes_and_balls_counter(attacker,defender)
                    game.show_result(attacker)
                    if sb_total == 2:
                        attacker.num_list = [6,8,9,0]
                        return attacker
                    elif sb_total == 3:
                        attacker.num_list = [5,8,9,0]
                        game.strikes_and_balls_counter(attacker,defender)
                        game.show_result(attacker)
                        if sb_total == 2:
                            attacker.num_list = [6,7,9,0]
                            return attacker
                        if sb_total == 4:
                            attacker.num_list = [5,8,9,0]
                            return attacker
                    elif sb_total == 4:
                        attacker.num_list = [5,7,9,0]
                        return attacker
                            
        elif sb_total == 1 :
            attacker.num_list = a.append(c)
            game.strikes_and_balls_counter(attacker,defender)
            game.show_result(attacker)
            if sb_total == 0:   D
            
            