#! python3
import numpy as np
from scipy.spatial.transform import Rotation
import pandas as pd
import sys


def angle_to_quat(angles, rotation='ZYX'):
    rot = Rotation.from_euler(rotation, angles, degrees=True) # x, y, z, w
    q = rot.as_quat()
    temp = q[3] # bring w to front
    q[1:] = q[:3]
    q[0] = temp
    return q #, rot.as_matrix() # w, x, y, z

if __name__ == "__main__":
    # Problems in degrees 
    # Given in phi, theta, psi (roll, pitch, yaw)
    # w i j k
    angles_file = "angles.txt"
    if len(sys.argv) > 1:
        angles_file = sys.argv[1]

    angles_df = pd.read_csv(angles_file, delimiter=" ")
    angles = angles_df.to_numpy()

    angles_ans = np.apply_along_axis(angle_to_quat, 1, angles)

    pd.DataFrame(angles_ans.round(4)).to_csv("problem_1_ans.txt", header=False, index=False, sep=" ")

    # yaw, pitch, roll
    # z, y, x