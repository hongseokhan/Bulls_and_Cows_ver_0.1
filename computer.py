import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.__defend_num_list = []
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.__w = 0
        self.__A= ['1','2']
        self.__B= ['3','4']
        self.__C= ['5','6']
        self.__D= ['7','8']
        self.__E= ['9','0']
        self.step_four_sb_cnt_total = 0
        
    @property
    def defend_num_list(self):
        return self.__defend_num_list
    
    @defend_num_list.setter
    def defend_num_list(self,num_list):
        self.__defend_num_list = num_list
        
    def _random_generator(self):
        self.__defend_num_list = [str(x) for x in random.sample(range(1,10),4)]

    def stage_one_update_sb_numbers(self, solving_steps):
        if solving_steps == 0:
            self.__x = self.balls + self.strikes
            return self.__x
        elif solving_steps == 1:
            self.__y = self.balls + self.strikes    
            return self.__y
        elif solving_steps == 2:
            self.__z = self.balls + self.strikes
            return self.__z
        elif solving_steps == 3:
            self.__w = self.balls + self.strikes
            return self.__w
        elif solving_steps == 4:
            self.step_four_sb_cnt_total = self.balls + self.strikes
            return self.step_four_sb_cnt_total
        elif solving_steps == 5:
            self.step_five_sb_cnt_total = self.balls + self.strikes
            return self.step_five_sb_cnt_total
        elif solving_steps == 6:
            self.step_six_sb_cnt_total = self.balls + self.strikes
            return self.step_six_sb_cnt_total
        elif solving_steps == 7:
            self.step_seven_sb_cnt_total = self.balls + self.strikes
            return self.step_seven_sb_cnt_total
        
            

    def _make_attack_num(self, solving_steps):
        if solving_steps == 0:
            return self.__A + self.__B
        elif solving_steps == 1:
            return self.__B + self.__C
        elif solving_steps == 2:
            return self.__C + self.__A
        elif solving_steps == 3:
            return self.__A + self.__D
        elif solving_steps == 4:
            step_four_list = self.stage_two_make_attack_num(solving_steps)
            return step_four_list
        elif solving_steps == 5:
            step_five_list = self.stage_two_make_attack_num(solving_steps)
            return step_five_list
        elif solving_steps == 6:
            step_six_list = self.stage_two_make_attack_num(solving_steps)
            return step_six_list
        elif solving_steps == 7:
            step_seven_list = self.stage_two_make_attack_num(solving_steps)
            return step_seven_list
        
    def stage_two_make_attack_num(self,solving_steps):
        A_sb_cnt = int((self.__x+self.__y+self.__z)/2 - self.__y)
        B_sb_cnt = int((self.__x+self.__y+self.__z)/2 - self.__z)
        C_sb_cnt = int((self.__x+self.__y+self.__z)/2 - self.__x)
        D_sb_cnt = int(self.__w-((self.__x+self.__y+self.__z)/2 -self.__y))
        E_sb_cnt = 4-(A_sb_cnt+B_sb_cnt+C_sb_cnt+D_sb_cnt)
        
        group_list = [self.__A,self.__B,self.__C,self.__D,self.__E]
        sb_cnt_group_list = [A_sb_cnt,B_sb_cnt,C_sb_cnt,D_sb_cnt,E_sb_cnt]
        test_candidates_list= []
        slice_test_candidates_list= []
        
        if solving_steps == 4:
            # [1,2,3,5]
            if len(set(sb_cnt_group_list)) == 3:
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 2:
                        test_candidates_list += [group_list[i][0],group_list[i][1]]
                        for j in range(len(sb_cnt_group_list)):
                            if sb_cnt_group_list[j] == 1:
                                test_candidates_list += str(group_list[j][0])
            
            elif len(set(sb_cnt_group_list)) == 2:
                # [1,3,9,0]
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 1:
                        test_candidates_list  += str(group_list[i][0])
                        for j in range(len(sb_cnt_group_list)):
                            test_candidates_list = test_candidates_list[0:2]
                            if sb_cnt_group_list[j] == 0:
                                test_candidates_list = test_candidates_list + [group_list[j][0],group_list[j][1]]
                    #[1,2,3,4]
                    elif sb_cnt_group_list[i] == 2:
                        test_candidates_list += [group_list[i][0],group_list[i][1]]
                        
            return test_candidates_list

        elif solving_steps == 5:
            #[1,2,3,6]
            if len(set(sb_cnt_group_list)) == 3:
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 2:
                        test_candidates_list += [group_list[i][0],group_list[i][1]]
                for j in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[j] == 1:
                        test_candidates_list += str(group_list[j][0])
            #[1,4,9,0]
            elif len(set(sb_cnt_group_list)) == 2:
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 1:
                        test_candidates_list  += str(group_list[i][0])
                for j in range(len(sb_cnt_group_list)):
                    slice_test_candidates_list = test_candidates_list[0:2]
                    if sb_cnt_group_list[j] == 0:
                        test_candidates_list = slice_test_candidates_list + [group_list[j][0],group_list[j][1]]
                        test_candidates_list = [int(x) for x in test_candidates_list]
                        for i in range(len(test_candidates_list)):
                            if i == 1:
                                test_candidates_list[i] += 1
                                test_candidates_list = [str(x) for x in test_candidates_list]
            return test_candidates_list

        elif solving_steps == 6:
            # [2,1,1,0,0] 인그룹 답찾기
            if len(set(sb_cnt_group_list)) == 3:
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 2:
                        test_candidates_list += [group_list[i][0],group_list[i][1]]
                for j in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[j] == 1:
                        if self.step_four_sb_cnt_total == 0:
                            test_candidates_list += str(group_list[j][1])
                        elif self.step_five_sb_cnt_total == 1:
                                test_candidates_list += str(group_list[j][0])
            #[9,0,5,7]
            elif len(set(sb_cnt_group_list)) == 2:
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 1:
                        test_candidates_list  += str(group_list[i][0])
                for j in range(len(sb_cnt_group_list)):
                    slice_test_candidates_list = test_candidates_list[2:4]
                    if sb_cnt_group_list[j] == 0:
                        test_candidates_list =  [group_list[j][0],group_list[j][1]] + slice_test_candidates_list
            return test_candidates_list
        
        elif solving_steps == 7:
            #[9,0,5,8]
            if len(set(sb_cnt_group_list)) == 2:
                for i in range(len(sb_cnt_group_list)):
                    if sb_cnt_group_list[i] == 1:
                        test_candidates_list  += str(group_list[i][0])
                for j in range(len(sb_cnt_group_list)):
                    slice_test_candidates_list = test_candidates_list[2:4]
                    if sb_cnt_group_list[j] == 0:
                        test_candidates_list = [group_list[j][0],group_list[j][1]] + slice_test_candidates_list
                        test_candidates_list = [int(x) for x in test_candidates_list]
                        for i in range(len(test_candidates_list)):
                            if i == 3:
                                test_candidates_list[i] += 1
                                test_candidates_list = [str(x) for x in test_candidates_list]
            return test_candidates_list
    
    
    
        
                                    
                        
            
                    