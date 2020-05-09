import pyautogui
from pynput.mouse import Listener
from PIL import Image
import numpy as np
import time



pyautogui.FAILSAFE = True  

count = 0
upleft = ()
downright = ()

def on_click(x, y, button, pressed):
    global count,upleft,downright
    if pressed:
        if(count == 0):
            upleft = (x,y)
        elif(count == 1):
            downright = (x,y)
            return False
        count+=1


with Listener(on_click=on_click) as listener:
    listener.join()


def distanceSquare(l1,l2):
    sum = 0
    for i in range(len(l1)):
        sum += (l1[i]-l2[i])*(l1[i]-l2[i])
    return sum


print(upleft)
print(downright)


sample_step = 15
step = 30


while(True):
    pic = np.asarray(pyautogui.screenshot())


    # print(pic.shape)
    # print(pic[upleft[1]][upleft[0]])

    #surface
    # sample_upleft = (281,820)     
    # sample_downright = (957,1530)
    # upleft = (281,820)     
    # downright = (957,1530)

    #PC
    sample_upleft = (260,470)     
    sample_downright = (670,890)
    upleft = (260,470)     
    downright = (670,890)

    colordict = {}
    for i in range(sample_upleft[1],sample_downright[1],sample_step):
        for j in range(sample_upleft[0],sample_downright[0],sample_step):
            color = tuple(pic[i][j])
            if(distanceSquare(color,(42,34,54))<100):
                continue
            elif(distanceSquare(color,(42,34,54))<100):
                continue
            elif(color!=tuple(pic[i+6][j]) or color!=tuple(pic[i-6][j]) or color!=tuple(pic[i][j+6]) or color!=tuple(pic[i][j-6])):
                continue
            else:
                if(color not in colordict):
                    colordict[color] = 0
                else:
                    colordict[color] += 1

    delList = []
    for key, value in colordict.items():
        if(value < 3):
            delList.append(key)
    for key in delList:
        del colordict[key]


    # print(colordict)   
    try:        

            

        max_key = max(colordict, key=colordict.get)
        del colordict[max_key]
        secondmax_key = max(colordict, key=colordict.get)
        print(secondmax_key)

        if( distanceSquare( (130,20,31) ,pic[931][302]) < 100 ):
            time.sleep(1)
            print('delay')


        find = False
        for i in range(upleft[1],downright[1],step):
            for j in range(upleft[0],downright[0],step):
                color = tuple(pic[i][j])
                if(distanceSquare(color,secondmax_key)<10):
                    pyautogui.click(x=j, y=i)
                    find = True
                    break
            if(find):
                break

    except:
        pass
    #    time.sleep(0.5)
                

    # time.sleep(0.1)
    # Image.fromarray(pic2).show()




            
    # break

