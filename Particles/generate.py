import json
with open('t.adofai', encoding='utf-8-sig') as f:
    T = json.load(f)

def toHex(r):
    return hex(r)[2:].rjust(2, '0')

def color(*c):
    return ''.join(map(toHex, c))

def move(pos, x, y, offset):
    global T
    T['actions'].append({
        "floor": 1, "eventType": "MoveTrack",
        "startTile": [55+pos, "ThisTile"], "endTile": [55+pos, "ThisTile"],
        "duration": 0, "positionOffset": [-26-pos+x, -y],
        "scale": 100, "angleOffset": 0.1*offset
    })

from pymunk import *
from time import sleep

ASDF = 60
shrink = 3/4
rad = 2*ASDF/3*shrink
w = 24*ASDF
h = 14*ASDF
cnt = 5

def add_body(space, idx):
    body = Body(1, 100, body_type = Body.DYNAMIC)
    body.position = ((idx//cnt+1)*rad+1, (idx%cnt)*rad+5)
    shape = Circle(body, rad)
    shape.density = 2
    shape.elasticity = 1.05
    space.add(body, shape)
    return body

space = Space()
space.gravity = (0, 500)
body = [add_body(space, i) for i in range(cnt*5)]

floor = Body(body_type = Body.STATIC)
shape = Segment(floor, (0, h), (w, h), 10)
space.add(floor, shape)

lwall = Body(body_type = Body.STATIC)
shape = Segment(lwall, (0, 0), (0, h), 10)
space.add(lwall, shape)

rwall = Body(body_type = Body.STATIC)
shape = Segment(rwall, (w, 0), (w, h), 25)
space.add(rwall, shape)

FPS = 30
frame = 0

while 1:
    if frame == 600: break
    if frame%FPS == 0: print(frame)
    space.step(1/FPS)
    sleep(0.03)
    frame += 1
    
    for i in range(25):
        pos = body[i].position
        move(i, round(pos.x/ASDF, 2), round(pos.y/ASDF, 2), frame/2)

with open('a.adofai', 'w') as f:
    f.write(json.dumps(T).replace(' ', ''))
