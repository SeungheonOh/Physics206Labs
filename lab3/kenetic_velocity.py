import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

import calibration

g = 9.8
mpp = calibration.calibrate()

wide = lambda x: "kenetic_wide_"+str(x)+"_.csv"
shallow = lambda x: "kenetic_shallow_"+str(x)+"_.csv"

tag = lambda x, y, r: r["position_px_"+str(x)+"-"+str(y)]

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def angle(x1, y1, x2, y2, x3, y3):
    v1 = [x2-x1, y2-y1]
    v2 = [x3-x1, y3-y1]
    return np.degrees(np.arccos(np.dot(v1, v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))))

def doThing(fname):
    trials = []
    for i in range(1, 10):
        df = pd.read_csv(fname(i))
        points = []
        angles = []
        for _, r in df.iterrows():
            time = r["timestamp"]
            (gx, gy) = tag("x", "green", r), tag("y", "green", r)
            (px, py) = tag("x", "hotpink", r), tag("y", "hotpink", r)
            (yx, yy) = tag("x", "yellowneon", r), tag("y", "yellowneon", r)
            (ox, oy) = tag("x", "darkorange", r), tag("y", "darkorange", r)
            if py > gy or gy > 700:
                continue
            if math.isnan(gx) or math.isnan(gy):
                continue

            val = {}
            val['time'] = time
            val['x'] = gx * mpp
            val['y'] = gy * mpp
            points.append(val)
            angles.append(angle(ox, oy, px, py, yx, yy))

        trials.append((points, np.average(angles)))
    return trials

def doThingg(fname):
    trials = doThing(fname)

    ks = []
    for trial, avgAngle in trials:
        # vector
        for i in range(0, len(trial) - 1):
            val1 = trial[i]
            val2 = trial[i + 1]
            td = (val2['time'] - val1['time']) / 1000
            vx = (val2['x'] - val1['x']) / td
            vy = (val2['y'] - val1['y']) / td
            trial[i]['vx'] = vx
            trial[i]['vy'] = vy

        # acceleration
        for i in range(0, len(trial) - 2):
            val1 = trial[i]
            val2 = trial[i + 1]
            td = (val2['time'] - val1['time']) / 1000
            ax = (val2['vx'] - val1['vx']) / td
            ay = (val2['vy'] - val1['vy']) / td
            a = math.sqrt(ax ** 2 + ay ** 2)
            trial[i]['ax'] = ax
            trial[i]['ay'] = ay
            trial[i]['a'] = a

        avgA = np.average(list(map(lambda x: x['a'], trial[:-2])))
        k = (avgA - np.sin(np.radians(avgAngle)) * g) / (- np.cos(np.radians(avgAngle)) * g)
        ks.append(k)
    return ks

wks = doThingg(wide)
sks = doThingg(shallow)

print("wide coefficients: ", wks)
print("wide coefficients avg: ", np.average(wks))
print("wide coefficient error: ", np.std(wks)/math.sqrt(len(wks)))
print()
print("shallow coefficients: ", sks)
print("shallow coefficients avg: ", np.average(sks))
print("shallow coefficient error: ", np.std(sks)/math.sqrt(len(sks)))
