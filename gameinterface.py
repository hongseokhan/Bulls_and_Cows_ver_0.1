from player import Player
from human import Human
from computer import Computer

class Gameinterface:
    
    def strikes_and_balls_counter(self,attacker,defender):
            

        for n,nvalue in enumerate(attacker.num_list):    
            for m,mvalue in enumerate(defender.num_list):
                if nvalue == mvalue:
                    if n == m:
                        attacker._strikes += 1
                    else:
                        attacker._balls += 1
        attacker.trys += 1


    def show_result(self,attacker):
        if attacker.strikes ==0 and attacker.balls == 0:
            print(f'<{attacker.trys}차 시도>, Nothing 입니다.')
            print('-----------------------------------------------')
        
        else:
            print(f'<{attacker.trys}차시도> {attacker.strikes}스트라이크 {attacker.balls}볼 입니다.')
            print('-----------------------------------------------')  
                
    def gamerun(self):
        
        mode = input('\n 게임모드를 선택하세요:    ')
        
        if mode == '1':
            print("PVC 대전모드입니다")
            player1 = Computer()
            player2 =  Human()
            print('player1의 숫자 4자리가 랜덤으로 발생하였습니다')
            player1._random_generator()
            print('player2의 4자리 숫자를 선택해주세요')
            player2._receive_input_num_list()
            attacker1 = Computer()
            while True:
                print('-----------------------------------------------')
                print('플레이어 1의 공격차례 입니다.')
                #attacker1._receive_input_num_list()
                self.strikes_and_balls_counter(attacker1,player2)
                player1.strikes = attacker1.strikes
                player1.balls = attacker1.balls
                player1.trys += attacker1.trys 
                self.show_result(player1)
                    
                    
                attacker2 = Human()
                print('플레이어 2의 공격차례 입니다.')
                attacker2._receive_input_num_list()
                self.strikes_and_balls_counter(attacker2,player1)
                player2.strikes = attacker2.strikes
                player2.balls = attacker2.balls
                player2.trys += attacker2.trys
                self.show_result(player2)
                if player1.strikes == 4 or player2.strikes == 4:
                    self._show_result(player1,player2)
                    break
                
        elif mode == '2':
            print("PVP 대전모드 입니다.")
            player1  =  Human()
            player2  = Human()
            print('player1의 4자리 숫자를 선택해주세요')
            player1._receive_input_num_list()
            player1.num_list
            print('player2의 4자리 숫자를 선택해주세요')
            player2._receive_input_num_list()
            player2.num_list
                
                
            while True:
                print('-----------------------------------------------')
                print('플레이어 1의 공격차례 입니다.')
                attacker1 = Human()
                attacker1._receive_input_num_list()
                self.strikes_and_balls_counter(attacker1,player2)
                player1.strikes = attacker1.strikes
                player1.balls = attacker1.balls
                player1.trys += attacker1.trys 
                self.show_result(player1)
                    
                    
                attacker2 = Human()
                print('플레이어 2의 공격차례 입니다.')
                attacker2._receive_input_num_list()
                self.strikes_and_balls_counter(attacker2,player1)
                player2.strikes = attacker2.strikes
                player2.balls = attacker2.balls
                player2.trys += attacker2.trys
                self.show_result(player2)
                if player1.strikes == 4 or player2.strikes == 4:
                    self._show_result(player1,player2)
                    break
                
                
    def _show_result(self,player1,player2):
        
        if player2.strikes == 4 and player1.strikes == 4:
            print('\n 동점입니다 다시 한번 붙어 보세요')
        
        elif player1.strikes == 4:
            print('\n player1님 축하합니다')
            print(f'{player1.trys}회 시도만에 성공 했습니다\n')
            print(f'player2 가지고 있는 숫자는 {player2.num_list}입니다')
            print('==============================================')
            print('\n player2님 아쉽습니다')
            print(f'{player2.trys}회 시도만에 게임에 패배 했습니다.')
            print(f'player1이 가지고 있는 숫자는 {player1.num_list}입니다')
        
        elif player2.strikes == 4:        
            print('\n player2님 축하합니다')
            print(f'{player2.trys}회 시도만에 성공 했습니다\n')
            print(f'player1 가지고 있는 숫자는 {player2.num_list}입니다')
            print('==============================================')
            print('\n player1님 아쉽습니다')
            print(f'{player1.trys}회 시도만에 게임에 패배 했습니다')
            print(f'player2 가지고 있는 숫자는 {player2.num_list}입니다')
            
                