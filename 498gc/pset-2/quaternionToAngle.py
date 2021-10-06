#! python3
import numpy as np
from scipy.spatial.transform import Rotation
import pandas as pd
import sys

def quat_to_angle(quat, rotation='zyx'):
    q = quat.copy()
    temp = q[0] # bring w to back
    q[:3] = q[1:]
    q[3] = temp
    ang = Rotation.from_quat(q)
    return ang.as_euler('ZYX', degrees=True) #, ang.as_matrix()

if __name__ == "__main__":
    quaternions_file = "quaternions.txt"
    if len(sys.argv) > 1:
        quaternions_file = sys.argv[1]

    quaternions_df = pd.read_csv(quaternions_file, delimiter=" ")
    quaternions = quaternions_df.to_numpy()

    quaternions_ans = np.apply_along_axis(quat_to_angle, 1, quaternions)

    pd.DataFrame(quaternions_ans.round(1)).to_csv("problem_2_ans.txt", header=False, index=False, sep=" ")