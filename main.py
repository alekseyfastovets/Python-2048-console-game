import random
import os
import time



def choseItem(filedLen):

	stats = []
	startItems = [2,2,2,2,2,2,2,2,2,4]

	for i in range(0,filedLen):
		stats.append([random.randint(0,filedLen-1),
					  random.randint(0,filedLen-1),
					  startItems[random.randint(0,9)]])

	return stats


def initField(filedLen):
    if filedLen > 10 or filedLen <=2:
        print('Размер поля не должен быть больше 10 и меньше 2\nЭто очевидно! В наказание, будет тебе маленькое поле, играй так.')
        filedLen = 2
    field = []
   
    for i in range(0,filedLen):
        elem = []
        for k in range(0,filedLen):
            elem.append(0)
        field.append(elem)
	
    stats = choseItem(filedLen)

    for val in stats:
        field[val[0]][val[1]] = val[2]

    return field




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

def scors(arr):
    scors = 0
    for i in arr:
        for k in i:
            scors = scors + k
    return int(scors)  


def firstOpen(fileForFile):
    os.system('cls')
    with open(fileForFile,'r') as file:
        for line in file:
            print(line, end = '\n')
        time.sleep(3)
        os.system('cls')
    

if __name__ == '__main__':

    firstOpen(r'res/load.txt')

    field = initField(int(input('Размер поля: ')))

    for i in field:
        print(i)    
        
    while True:
        print("Количество очков:", scors(field), sep=' ', end=' ')
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
            
        
            
            
        
        
        

            
            
        