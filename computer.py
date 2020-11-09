import random
from player import Player


class Computer(Player):

    def __init__(self):
        super().__init__()
        self._answer_candidates
        self.__x
        self.__y 
        self.__z 
        self.__w 

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
            
    def _update_sb_numbers(self, solving_steps):
        if solving_steps == 0:
            self.__x = self.balls = self.strikes
        elif solving_steps == 1:
            self.__y = self.balls = self.strikes
        elif solving_steps == 2:
            self.__z = self.balls = self.strikes
        elif solving_steps == 3:
            self.__w = self.balls = self.strikes


    def _make_attack_num(self, solving_steps):
        if solving_steps == 0:
            return [1,2,3,4]
        elif solving_steps == 1:
            return [3,4,5,6]
        elif solving_steps == 2:
            return [5,6,1,2]
        elif solving_steps == 3:
            return [1,2,7,8]
        elif solving_steps == 4:
            preapre_step_two(x, y, z, w)
            solve_step_two()
        elif
            solve_step_three()

    def preapre_step_two(self, x, y, z, w):
        A = (x+y+z)/2 - y
        B = (x+y+z)/2 - z
        C = (x+y+z)/2 - x
        D = w - ((x+y+z)/2 - y)
        if (A+B+C+D) != 4:
            E = 4-(A+B+C+D)
        self._answer_candidates = (A, B, C, D, E)
    
    def solve_step_two(self):
        self._answer_candidates
        # check_answer_candidates()
        num_two == ;
        num_one == ;
        if num_two == 2:

        elif num_two == 1 && num_one == 2:

        elif num_one == 4:

    def solve_step_three(self):