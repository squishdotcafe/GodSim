#Game of Life
#In game statistics based on real life
#V0.1
#Main Author Luke Dunn
#Others Involved:
#youtube.com/user/Mooshimity (myemailistemporary@gmail.com) added 48 lines of code
#youtube.com/user/Willbl3pic101 (william@williambl.com) added 8 lines of code
#someone else (xxx@email.com) added x lines of code
import time
import turtle
import antigravity
from datetime import datetime
from random import randint

tag = 0
runs = 0
gametime = "%s/%s/%s" % (now.day, now.month, now.year) #setting time to IRL time
#Please look at the errors you have made. I don't know if it works on your PC, but it won't run on mine for these errors:
#Traceback (most recent call last):
#File "C:\Users\Luke\Documents\GitHub\GodSim\World Simulator.py", line 17, in <module>
#gametime = "%s/%s/%s" % (now.day, now.month, now.year) #setting time to IRL time
#NameError: name 'now' is not defined
print("[Luke Dunn's Game of Life]")
time.sleep(0.1)
print()
#Temperature
print("[Select an average temperature of the region. (Celcius)]")
tmp = int(input())
ox = 0
co = 0
ni = 0
ar = 0
ot = 0
tmpd = 1
tmpb = 1
print()
#Population
print("[Select an estimated population of the region. (1-1000)]")
ppl = int(input())
ppla = ppl
ppld = 0
pplb = 0
ppli = 0
print()
#Development
print("[Select a stage of development for the region. (1-5)]")
dlp = int(input())
print()
#
#
#
print()
active = 1
while active == 1:
    cycle = 1
    while cycle < runs+1:
        print(cycle)
        cycle = cycle+1
        #Day
        print('"The day is " + gametime')
        #Add code to change day...
        #Population
        meechance = randint(0,1000) #Mass Extinction Event Chance is one in 1001.
        if meechance == 5:
            ppla = 0
            ppld = ppl
        if ppl < 2.5:
            ppla = 0
            ppld = ppl
        if ppla > 1:
            ppld = (ppld+(ppla*1.00009))*tmpd
            pplb = pplb+(ppla*1.00019)*tmpb
            ppla = ppl+int(pplb)-int(ppld)
        if ppla < 0:
            ppla = 0
        if pplb < 0:
            pplb = 0
        if ppla == 0:
            ppld = ppl+pplb
        #Atmosphere
        tmp = tmp*1.00000000000924426
        tmpd = tmp*1.000476190476
        tmpb = tmp*0.000476190476
        if tmpd < 0:
            tmpd = 2-tmp
        if tmpb < 0:
            tmpb = 2-tmp
        time.sleep(1/runs)
    time.sleep(1)
    print("[Type /help <page number> for commands to display]")
    command = 1
    while command == 1:
        cmd,tag = input().split()
        if cmd == '/help':
            print("##Generic")
            print("  /run <number of cycles>")
            print("  /help")
            print()
            print("##Stats")
            print("  /stats population")
            print("  /stats atmosphere")
            print("  /stats development")
            print()
            print("##Graph")
            print("  /graph population")
            print("  /graph atmosphere")
            print("  /graph development")
        ##Generic
        if cmd == '/run':
            runs = int(tag)
            command = 0
        ##Stats
        if cmd == '/stats':
            if tag == 'population':
                print('Deaths:',int(ppld))
                print('Alive: ',int(ppla))
                print('Born:  ',int(pplb))
                print()
            if tag == 'atmosphere':
                print('Temperature:',tmp,'*C')
                print()
                print('Carbon Dioxide %:',co)
                print('Oxygen %        :',ox)
                print('Nitrogen %      :',ni)
                print('Argon %         :',ar)
                print('Other %         :',ot)
                print()
        ##Graph
        if cmd == '/graph':
            if tag == 'population':
                turtle.speed(0)
                turtle.hideturtle()
                turtle.color('white')
                turtle.left(90)
                turtle.forward(500)
                turtle.right(180)
                turtle.color('black')
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(180)
                turtle.right(90)
                turtle.forward(10)
                turtle.left(90)
                turtle.color('red')
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.color('black')
                turtle.forward(10)
                turtle.left(90)
                turtle.color('blue')
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.color('black')
                turtle.forward(10)
                turtle.left(90)
                turtle.color('green')
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.color('black')
                turtle.forward(10)
                turtle.exitonclick()
