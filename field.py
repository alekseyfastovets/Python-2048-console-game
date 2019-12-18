from cell import cell2048
import random

class field2048(cell2048):
    def __init__(self,place = 3, cells = 3):
        super().__init__()
        self.field = []
        self.place = place
        self.creatField()
        self.firstStart(cells)
        
    def getField(self):
        return self.field
        
    def creatField(self):
        self.field = [[] for item in range(0,self.place)]
        for key,item in enumerate(self.field):
            self.field[key] = [self.creatCell() for item in range(0,self.place)]
        return self.field
            
    def firstStart(self, cells):
        status = []
        for i in range(0,cells):
            inState = True
            while inState:
                chouseCell = []
                cordX = random.randint(0, (self.place-1))
                chouseCell.append(cordX)
                cordY = random.randint(0, (self.place-1))
                chouseCell.append(cordY)
                if chouseCell in status:
                    continue
                else:
                    status.append(chouseCell)
                    inState = False
                
        for items in status:
            self.field[items[0]][items[1]] = 2
            
            
            
            
if __name__ == '__main__':
    obj = field2048()
    for i in obj.field:
        print(i)
        
            
    
        
        
        