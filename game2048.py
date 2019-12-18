from field import field2048
import random


class game2048(field2048):
    
    def __init__(self,field = 5, cells = 3):
        super().__init__(field, cells)
                

    def vertical(self,arr, direction):
        for i in range(len(arr)):
            preArr = []

            for item in arr:
                preArr.append(item[i])

            while preArr.count(0) != 0:
                preArr.remove(0)

            if direction.lower() == 'down':     
                preArr = preArr[::-1]

            for key in range(len(preArr)):
                if (key+1) < len(preArr):
                    if preArr[key] == preArr[key+1]:
                        preArr[key] = int(preArr[key])*2
                        preArr.pop(key+1)
                    else:
                        continue
                else:
                    break       

            while len(preArr) != len(arr):
                preArr.append(0) 

            if direction.lower() == 'down':     
                preArr = preArr[::-1]   

            for key, value in enumerate(preArr):
                arr[key][i] = value

        arr, cont = self.nextStep(arr)

        return arr, cont


    def horizontal(self,arr,direction):
        for i, elem in enumerate(arr):
            while elem.count(0) != 0:
                elem.remove(0)

            if direction.lower() == 'right':     
                elem = elem[::-1]

            for key in range(len(elem)):
                if (key+1) < len(elem):
                    if elem[key] == elem[key+1]:
                        elem[key] = int(elem[key])*2
                        elem.pop(key+1)
                    else:
                        continue
                else:
                    break

            while len(elem) != len(arr):
                elem.append(0)

            if direction.lower() == 'right':     
                elem = elem[::-1]

            arr[i] = elem

        arr, cont = self.nextStep(arr)
          
        return arr, cont


    def nextStep(self,arr):
        coords = []
        for key, value in enumerate(arr):
            while value.count(0) != 0:
                index = value.index(0)
                data = str(key)+'.'+str(index) 
                coords.append(data)
                value[index] = '*'
            while value.count('*') != 0:
                index = value.index('*')
                value[index] = 0
        if len(coords) != 0:        
            index = random.choice(coords)
            coordX = int(index[0])
            coordY = int(index[2])
            arr[coordX][coordY] = 2
            game = 'Game Must Go On!'
            return arr, game
        else:
            game = 'Game Over!'
            return arr, game

         
            
        
if __name__ == '__main__':
    
    obj = game2048(3,2)
    data = obj.field 
    
    for i in data:
        print(i)
    print(['_']*20)
    data, status = obj.horizontal(obj.field, 'left')
    
    for i in data:
        print(i)

        