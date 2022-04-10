import time
import os
import random

os.system("cls")
programa = True
x1 = 1
x2 = 3
y1 = 1
y2 = 3
def pelota():
    time.sleep(0.05)
    os.system('cls')
    print("\n"*y," "*x,"*") 
while programa == True:
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    while bajando == True:
        x1 += 1
        x2 += 1
        

    if y1 and y2 < 20:
        y1 += 1
        y2 += 1
