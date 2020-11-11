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
        

    def _update_sb_numbers(self, solving_steps):
        if solving_steps == 0:
            self.__x = self.balls + self.strikes
        elif solving_steps == 1:
            self.__y = self.balls + self.strikes
        elif solving_steps == 2:
            self.__z = self.balls + self.strikes
        elif solving_steps == 3:
            self.__w = self.balls + self.strikes


    def _make_attack_num(self, solving_steps):
        A= ['1','2']
        B= ['3','4']
        C= ['5','6']
        D= ['7','8']
        E= ['9','0']
        if solving_steps == 0:
            return A.append(B)
        elif solving_steps == 1:
            return B.append(C)
        elif solving_steps == 2:
            return C.append(A)
        elif solving_steps == 3:
            return A.append(D)
        elif solving_steps == 4:
            prepare_step_two(x, y, z, w)
            solve_step_two()
        #elif:
        #   solve_step_three()

    def prepare_step_two(self, x, y, z, w):
        A_sb_cnt = (x+y+z)/2 - y
        B_sb_cnt = (x+y+z)/2 - z
        C_sb_cnt = (x+y+z)/2 - x
        D_sb_cnt = w-((x+y+z)/2 -y)
        E_sb_cnt = 4-(A_sb_cnt+B_sb_cnt+C_sb_cnt+D_sb_cnt)
        
        sb_cnt_group_list = [A_sb_cnt,B_sb_cnt,C_sb_cnt,D_sb_cnt,E_sb_cnt]
        
        for i in len(sb_cnt_group_list):
            if sb_cnt_group_list[i] == 2:
                
        
            
    #def solve_step_three(self):