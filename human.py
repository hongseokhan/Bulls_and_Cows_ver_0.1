from player import Player

class Human(Player):
    
    def __init__(self):
        super().__init__()
    
    @property
    def num_list(self):
        return self._num_list
    
    @num_list.setter
    def input_num_list(self,num_list):
        self._num_list = num_list   
    
    def input_rule(self,num_list):
        flag = True
        message = []
    
        if not(num_list.isdecimal()):
            flag = False
            message = f'{num_list}는 숫자가 아닙니다.'

        elif len(num_list) != 4:
            flag = False
            message = f'{num_list}는 4자리 숫자가 아닙니다.'
    
        elif len(num_list) != len(set(num_list)):
            flag = False
            message = f'{num_list}는 중복된 숫자가 존재 합니다'
            

        return flag, message
    
    def _receive_input_num_list(self):
        flag = False
        
        while flag is False:
            self._num_list = input('4자리 숫자를 입력하세요:')
        
            flag, message = self.input_rule(self._num_list)
            if flag is False:
                print(message)
            
        
        