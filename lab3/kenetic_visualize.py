import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

wide = lambda x: "kenetic_wide_"+str(x)+"_.csv"
shallow = lambda x: "kenetic_shallow_"+str(x)+"_.csv"

tag = lambda x, y, r: r["position_px_"+str(x)+"-"+str(y)]

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def angle(x1, y1, x2, y2, x3, y3):
    v1 = [x2-x1, y2-y1]
    v2 = [x3-x1, y3-y1]
    return np.degrees(np.arccos(np.dot(v1, v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))))

testss = []
def doThing(fname):
    tests = []
    for i in range(1, 10):
        print(fname(i))
        df = pd.read_csv(fname(i))
        test = []
        for _, r in df.iterrows():
            (gx, gy) = tag("x", "green", r), tag("y", "green", r)
            (px, py) = tag("x", "hotpink", r), tag("y", "hotpink", r)
            (yx, yy) = tag("x", "yellowneon", r), tag("y", "yellowneon", r)
            (ox, oy) = tag("x", "darkorange", r), tag("y", "darkorange", r)
            if py > gy or gy > 700:
                continue
            test.append((gx, gy))
        tests.append(test)
    testss.append(tests)

doThing(wide)
doThing(shallow)

i = 0
plt.title("Block motion visualized")
for t in testss:
    for tt in t:
        xs, ys = zip(*tt)
        plt.plot(xs, ys, label=str(i))
plt.show()
