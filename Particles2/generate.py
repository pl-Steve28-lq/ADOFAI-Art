import json
with open('t.adofai', encoding='utf-8-sig') as f:
    T = json.load(f)

def toHex(r):
    return hex(r)[2:].rjust(2, '0')

def color(*c):
    return ''.join(map(toHex, c))

def move(pos, x, y, t, s=100):
    global T
    T['actions'].append({
        "floor": 1, "eventType": "MoveTrack",
        "startTile": [80+pos, "ThisTile"], "endTile": [80+pos, "ThisTile"],
        "duration": 0, "positionOffset": [x-pos-1, -1-y], "angleOffset": 0.1*t, "scale": s
    })

from sys import exit
from pymunk import *
from random import randint

ASDF = 60
rad = 2*ASDF/3
w = 24*ASDF
h = 14*ASDF
cnt = 7

def add_body(space, idx):
    v = int((2*idx+1/4)**.5-1/2) + 1
    u = idx - v*(v-1)//2
    body = Body(1, 100, body_type = Body.DYNAMIC)
    body.position = (w//2+v*90, h//2-90*(u-v//2+(1-v%2)/2)+randint(0, 5)/5)
    shape = Circle(body, rad)
    shape.density = 0.1
    shape.elasticity = 1.05
    space.add(body, shape)
    return body

space = Space()

ball = Body(1, 100, body_type = Body.DYNAMIC)
ball.position = (w//7, h//2)
shape = Circle(ball, 1.333*rad)
shape.density = 2
shape.elasticity = 1.05
space.add(ball, shape)
ball.velocity = (700, 0)

body = [add_body(space, i) for i in range(cnt*(cnt+1)//2)]

floor = Body(body_type = Body.STATIC)
shape = Segment(floor, (0, h), (w, h), 5)
space.add(floor, shape)

floor = Body(body_type = Body.STATIC)
shape = Segment(floor, (0, 0), (w, 0), 5)
space.add(floor, shape)

lwall = Body(body_type = Body.STATIC)
shape = Segment(lwall, (0, 0), (0, h), 5)
space.add(lwall, shape)

rwall = Body(body_type = Body.STATIC)
shape = Segment(rwall, (w, 0), (w, h), 5)
space.add(rwall, shape)

FPS = 60
frame = 0

while 1:
    if frame == FPS*20: break
    if frame%2:
        for i, v in enumerate(body):
            pos = v.position
            x, y = pos.x, pos.y
            move(i, round(x/ASDF, 3), round(y/ASDF, 3), frame//2)
        pos = ball.position
        x, y = pos.x, pos.y
        move(28, round(x/ASDF, 3), round(y/ASDF, 3), frame//2, 150)
    space.step(1/FPS)
    frame += 1

with open('a.adofai', 'w') as f:
    f.write(json.dumps(T).replace(' ', ''))
