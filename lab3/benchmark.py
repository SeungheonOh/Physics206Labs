import pandas as pd
import numpy as np

# 'frame_no', 'timestamp', 'size_px-darkorange',
#        'position_px_x-darkorange', 'position_px_y-darkorange', 'rx-darkorange',
#        'ry-darkorange', 'vx-darkorange', 'vy-darkorange', 'ax-darkorange',
#        'ay-darkorange', 'size_px-green', 'position_px_x-green',
#        'position_px_y-green', 'rx-green', 'ry-green', 'vx-green', 'vy-green',
#        'ax-green', 'ay-green', 'size_px-hotpink', 'position_px_x-hotpink',
#        'position_px_y-hotpink', 'rx-hotpink', 'ry-hotpink', 'vx-hotpink',
#        'vy-hotpink', 'ax-hotpink', 'ay-hotpink', 'size_px-lightorange',
#        'position_px_x-lightorange', 'position_px_y-lightorange',
#        'rx-lightorange', 'ry-lightorange', 'vx-lightorange', 'vy-lightorange',
#        'ax-lightorange', 'ay-lightorange', 'size_px-yellowneon',
#        'position_px_x-yellowneon', 'position_px_y-yellowneon', 'rx-yellowneon',
#        'ry-yellowneon', 'vx-yellowneon', 'vy-yellowneon', 'ax-yellowneon',
#        'ay-yellowneon'

# for i in range(1, 9):
#     print(i)
#     a = pd.read_csv("kenetic_shallow_"+str(i)+"_.csv")

#     print(a.columns)

