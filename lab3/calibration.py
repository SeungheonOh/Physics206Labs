import pandas as pd
import numpy as np
import math

def calibrate():
    def dist(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    df = pd.read_csv("calibration.csv")

    dists = []
    for _, row in df.iterrows():
        dists.append(dist(row['position_px_x-green'], row['position_px_y-green'], row['position_px_x-hotpink'], row['position_px_y-hotpink']))

    avgDist = np.average(list(filter(lambda x: not math.isnan(x),dists)))

    return 0.2 / avgDist

if __name__ == "__main__":
    print("Meter per pixel:", calibrate())
