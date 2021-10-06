#! python3
import numpy as np
from scipy.spatial.transform import Rotation

def r_to_q(angle, degrees=True):
    phi = np.pi * angle[0] / (180)
    theta = np.pi * angle[1] / (180)
    psi = np.pi * angle[2] / (180)

    R_phi = np.array([
        [1, 0, 0],
        [0, np.cos(phi), np.sin(phi)],
        [0, -np.sin(phi), np.cos(phi)]
    ])

    R_theta = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])

    R_psi = np.array([
        [np.cos(psi), np.sin(psi), 0],
        [-np.sin(psi), np.cos(psi), 0],
        [0, 0, 1]
    ])

    R = R_phi @ R_theta @ R_psi # R_x @ R_y @ R_z
    # R = R_psi @ R_theta @ R_phi

    e, v = la.eig(R)
    u = v[:,0]
    print(u)
    trace = R[0,0] + R[1,1] + R[2,2]
    theta = np.arccos((trace - 1)/2)
    q = np.zeros(4)
    q[0] = np.cos(theta/2)
    q[1] = u[0]*np.sin(theta/2)
    q[2] = u[1]*np.sin(theta/2)
    q[3] = u[2]*np.sin(theta/2)
    return q, R

def q_to_r(q):
    R = np.zeros((3,3))
    R[0,0] = 2*(q[0]**2 + q[1]**2) - 1
    R[0,1] = 2*(q[1]*q[2] - q[0]*q[3])
    R[0,2] = 2*(q[1]*q[3] + q[0]*q[2])

    R[1,0] = 2*(q[1]*q[2] + q[0]*q[3])
    R[1,1] = 2*(q[0]**2 + q[2]**2) - 1
    R[1,2] = 2*(q[2]*q[3] - q[0]*q[1])

    R[2,0] = 2*(q[1]*q[3] - q[0]*q[2])
    R[2,1] = 2*(q[2]*q[3] + q[0]*q[1])
    R[2,2] = 2*(q[0]**2 + q[3]**2) - 1

    return R