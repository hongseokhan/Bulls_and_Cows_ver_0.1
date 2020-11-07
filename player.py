class Player:
    
    def __init__(self):
        self._strikes = 0
        self._balls = 0 
        self._score = 1000
        self._trys = 0
        self._num_list = []
        
        
    @property
    def strikes(self):
        return self._strikes
    
    @strikes.setter
    def strikes(self,strikes):
        self._strikes = strikes

    @property
    def balls(self):
        return self._balls
    
    @balls.setter
    def balls(self,balls):
        self._balls = balls
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        self._score = score
    
    @property
    def trys(self):
        return self._trys
    
    @trys.setter
    def trys(self,trys):
        self._trys = trys