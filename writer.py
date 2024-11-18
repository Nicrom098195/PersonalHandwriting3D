import matplotlib.pyplot as plt
import json
from random import randint as rint

downZ=13.2
upZ=15
startGC="G28\nG1 Z"+str(upZ)+"\n"
endGC="G1 X0 Y0 Z"+str(upZ)+"\nG28 X\nM84\nM84"
sx=10
sy=80
text="Ciao Titti!\nCome va?"
speed=3000

with open('font.json', 'r') as file:
    data = json.load(file)

def show(punti, connect_lines=True):
    x = [p[0] for p in punti]
    y = [p[1] for p in punti]
    
    plt.figure(figsize=(8, 6))
    
    if connect_lines:
        plt.plot(x, y, linestyle='-', color='b', label="Lines")
    else:
        plt.scatter(x, y, color='r', label="Points")
    plt.title("Preiew")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

def gcode(frase):
    gc=startGC+"\n"
    for p in frase:
        gc+="G0 X"+str(p[0])+" Y"+str(p[1])+" Z"+str(p[2])+" F"+str(speed)+"\n"
    gc+=endGC
    return gc

def convert(t, height=10, fixedspacing=0):
    txt=t.replace("à", "a'").replace("è", "e'").replace("ì", "i'").replace("ò", "o'").replace("ù", "u'").replace("À", "A'").replace("È", "E'").replace("Ì", "I'").replace("Ò", "O'").replace("Ù", "U'").replace("\"", "''").replace("”", "''").replace("“", "''").replace("’", "'")
    punti=[]
    x=sx
    xc=0
    y=sy
    z=upZ
    for p in txt:
        if p == "\n":
            y+=15*height/10
    
    for p in txt:
        if p == "\n":
            y-=15*height/10
            x=sx
        elif p == " ":
            x+=6*height/10
        else:
            ind=rint(0, len(data[p])-1)
            for punto in data[p][ind]:
                if punto[0] == "START":
                    punti.append(((punto[1][0]*height/10)+x, (punto[1][1]*height/10)+y, upZ))
                    z=downZ
                elif punto[0] == "NORMAL":
                    z=downZ
                else:
                    z=upZ
                punti.append(((punto[1][0]*height/10)+x, (punto[1][1]*height/10)+y, z))
                xc=max(xc, (punto[1][0]*height/10)-1)
            if fixedspacing:
                x+=fixedspacing
            else:
                x+=xc+2
                xc=0
    return punti