import numpy as np
import pandas as pd
import math

wide = lambda x: "example_"+str(x)+"_.csv"
shallow = lambda x: "static_shallow_"+str(x)+"_.csv"

tag = lambda x, y, r: r["position_px_"+str(x)+"-"+str(y)]

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def angle(x1, y1, x2, y2, x3, y3):
    v1 = [x2-x1, y2-y1]
    v2 = [x3-x1, y3-y1]
    return np.degrees(np.arccos(np.dot(v1, v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))))

MOVEMENT_THRESHOLD = 50

def doThing(fname):
    angles = []
    for i in range(1, 10):
        df = pd.read_csv(fname(i))

        greenPinkDists = []
        for _, r in df.iterrows():
            gpdist = dist(tag("x", "green", r), tag("y", "green", r), tag("x", "hotpink", r), tag("y", "hotpink", r))
            if math.isnan(gpdist):
                continue

            if len(greenPinkDists) == 0:
                greenPinkDists.append(gpdist)
                continue

            if abs(np.average(greenPinkDists) - gpdist) > MOVEMENT_THRESHOLD:
                angles.append(angle(tag("x", "darkorange", r),
                                    tag("y", "darkorange", r),
                                    tag("x", "hotpink", r),
                                    tag("y", "hotpink", r),
                                    tag("x", "yellowneon", r),
                                    tag("y", "yellowneon", r)))       
                break
            else:
                greenPinkDists.append(gpdist)
            
    return angles


w = doThing(wide)
s = doThing(shallow)

print("shallow angles: ", s, "\nAverage: ", np.average(s))
print("shallow coefficent of friction: ", np.tan(np.radians(np.average(s))))
print("wide angles: ", w, "\nAverage: ", np.average(w))
print("wide coefficent of friction: ", np.tan(np.radians(np.average(w))))

