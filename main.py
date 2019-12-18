import random
import os


field = [[2,0,0,0],
         [0,0,0,2],
         [2,0,0,2],
         [0,0,0,0]]

for i in field:               
    print(i)



def vertical(arr, direction):
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
            
    arr, cont = nextStep(arr)
    print(cont)    
    return arr




def horizontal(arr,direction):
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
    
    arr, cont = nextStep(arr)
    print(cont)  
    return arr
 
    
def nextStep(arr):
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
        game = 'Game Must Go On'
        return arr, game
    else:
        game = 'Game Over'
        return arr, game

    
    

if __name__ == '__main__':    
        
    while True:
        step = input('Ход: ')
        os.system('cls')
        #os.system(['clear', 'cls'][os.name == os.sys.platform])
        if step == 'w':
            for i in vertical(field, 'up'):               
                print(i)
        elif step == 's':
            for i in vertical(field, 'down'):              
                print(i)
        elif step == 'a':
            for i in horizontal(field,'left'):              
                print(i)
        elif step == 'd':
            for i in horizontal(field,'right'):            
                print(i)
        else:
            break
            
        
            
            
        
        
        

            
            
        