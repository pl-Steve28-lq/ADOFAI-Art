import json
with open('t1.adofai', encoding='utf-8-sig') as f:
    h = json.load(f)

theta = 0
rad = 0
offset = 0

def getRadius():
    return 5*cos(rad)/2 + 4

from math import sin, cos
pi = 3.14

def getPos(i):
    t = pi*i/18
    r = getRadius()
    
    return (12+r*cos(t)*sin(theta)-i, r*sin(t))

def getData(i, offset):
    x, y = getPos(i)
    return { "floor": 1, "eventType": "MoveTrack", "startTile": [i+1, "ThisTile"], "endTile": [i+1, "ThisTile"],
      "duration": 0, "positionOffset": [int(x*10000)/10000, int(y*10000)/10000], "rotationOffset": 0, "scale": 100, "opacity": 100,
      "angleOffset": offset, "ease": "Linear", "eventTag": "" }

while theta < 12*pi+pi/2+0.2:
    for i in range(36):
        h["actions"].append(getData(i, offset))
    theta += 0.1
    rad += 0.1
    offset += 0.1

with open('testing.adofai', 'w') as f:
    json.dump(h, f)
