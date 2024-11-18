from writer import *
import sys

inf=None
text=None
height=10
out="result.gcode"
space=0

if "-in" in sys.argv:
    inf=sys.argv[sys.argv.index("-in")+1]
elif "-txt" in sys.argv:
    text=sys.argv[sys.argv.index("-txt")+1]
else:
    try:
        text=sys.argv[1]
    except:
        inf="text.txt"

if "-out" in sys.argv:
    out=sys.argv[sys.argv.index("-out")+1]
else:
    try:
        out=sys.argv[2]
    except:
        out="out.gcode"

ocont=""


if "-size" in sys.argv:
    height=float(sys.argv[sys.argv.index("-size")+1])

if "-space" in sys.argv:
    space=float(sys.argv[sys.argv.index("-space")+1])

if inf:
    with open(inf, "r", encoding="utf-8") as f:
        ocont=convert(f.read(), height, space)
else:
    ocont=convert(text, height, space)

gc=gcode(ocont)

with open(out, "w") as f:
    f.write(gc)

if "--show" in sys.argv:
    show(ocont, False)
if "--showl" in sys.argv:
    show(ocont, True)