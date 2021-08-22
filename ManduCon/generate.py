import json
with open('t1.adofai', encoding='utf-8-sig') as f:
    h = json.load(f)

def toHex(r):
    return hex(r)[2:].rjust(2, '0')

def color(*c):
    return ''.join(map(toHex, c))

from PIL import Image
import numpy as np
f1 = np.array(Image.open('f1.jpg'))
f2 = np.array(Image.open('f2.jpg'))

for w in range(7):
    tile = 0
    file = f1 if w%2 else f2
    another = f2 if w%2 else f1
    for u, i in enumerate(file):
        for v, (r, g, b, *_) in enumerate(i):
            tile += 1
            R1, G1, B1, *_ = file[u][v]
            R2, G2, B2, *_ = another[u][v]
            if (R1, G1, B1) == (R2, G2, B2): continue
            r, g, b = map(int, (r, g, b))
            if r+g+b < 30: r, g, b = 0, 0, 0
            if r+g+b > 740: r, g, b = 255, 255, 255
            h['actions'].append({
                "floor": 1, "eventType": "RecolorTrack", "startTile": [tile, "Start"], "endTile": [tile, "Start"],
                "trackColor": color(r, g, b),
                "trackColorAnimDuration": 0,
                "trackStyle": "Gems", "angleOffset": w
            })
with open('a.adofai', 'w') as f:
    json.dump(h, f)
