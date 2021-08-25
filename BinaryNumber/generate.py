import json
with open('t.adofai', encoding='utf-8-sig') as f:
    T = json.load(f)

def toHex(r):
    return hex(r)[2:].rjust(2, '0')

def color(*c):
    return ''.join(map(toHex, c))

def add(a):
    global T
    T['actions'].append(a)

def addCond(floor):
    add({ "floor": floor, "eventType": "SetConditionalEvents", "missTag": f'{floor}' })

def addText(x, y, text):
    add({ "floor": 9, "eventType": "AddText", "decText": f'{text}', "position": [x, y] })

def moveCamera(f):
    add({ "floor": f, "eventType": "MoveCamera",
        "duration": 0, "relativeTo": "LastPosition",
        "position": [0, -6*2**(f-1)], "eventTag": f'{f}'
    })

for i in range(255):
    addText(-4.5, 1.5-6*i, i)
    b = bin(i)[2:].rjust(8, '0')
    for j in range(8):
        addText(-8+j, 2.3-6*i, b[j])
for i in range(8):
    addCond(i+1)
    moveCamera(i+1)

with open('a.adofai', 'w') as f:
    f.write(json.dumps(T).replace(' ', ''))
