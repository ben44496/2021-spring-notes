import numpy as np
import matplotlib.pyplot as plt

def u1(time, dt):
    # delta_theta, delta_throttle
    return np.array([0, 0.5])

def u2(time, dt):
    # delta_theta, delta_throttle
    t = time * dt
    return np.array([0.5*np.sin(0.5*t), 0.5])

def u3(time, dt):
    t = time * dt
    return np.array([5*np.sin(0.5*t), 0.5])

def u4(time, dt):
    t = time * dt
    return np.array([0.5*np.sin(5*t), 0.5])

def u5(time, dt):
    t = time * dt
    return np.array([5*np.sin(5*t), 0.5])

def z_dot(z, u, t, dt):
    """Calculate Step at delta t
    z - Numpy array with shape (4,) representing [x, y, theta, vel]
    u - Numpy array with shape (2,) representing [delta_theta, delta_throttle]
    """
    x_dot = z[3]*np.cos(z[2])       # x_dot = v*cos(theta)
    y_dot = z[3]*np.sin(z[2])       # y_dot = v*sin(theta)
    theta_dot = -0.5*z[2] + u(t, dt)[0]    # theta_dot = -0.5*theta + delta_theta
    v_dot = -0.3*z[3] + u(t, dt)[1]        # v_dot = -0.3*v + delta_throttle
    z_dot = np.array([x_dot, y_dot, theta_dot, v_dot])
    return z_dot

def run_simulation(z_1, T, u, dt=0.1):
    # Initialize variables
    num_steps = int(np.ceil(T / dt))
    z = z_1.copy()
    x = []
    y = []

    # Append start points
    x.append(z[0])
    y.append(z[1])

    # Run simulation
    for t in range(1, num_steps):
        dzdt = z_dot(z, u, t, dt)
        z += dzdt * dt      # euler integration
        x.append(z[0])
        y.append(z[1])
    
    ax = plt.gca()
    ax.plot(x, y)
    ax.grid(True)
    
    return ax, x, y

if __name__ == "__main__":
    # Question 1
    z_0 = np.array([0,0,0,0], dtype=np.float64)   # Starting condition
    T = 30                      # Total Time
    u = u1      # delta_theta, delta_throttle

    fig = plt.figure(1)
    ax = run_simulation(z_0, T, u)
    plt.title("Map of Path Q1")
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)

    # Question 2
    z_0 = np.array([0,0,0,0], dtype=np.float64)
    T = 100                      # Total Time
    u = u2      # delta_theta, delta_throttle

    fig2 = plt.figure(2)
    ax2 = run_simulation(z_0, T, u)
    plt.title("Map of Path Q2")

    # Question 3: Amplitude increase
    z_0 = np.array([0,0,0,0], dtype=np.float64)
    T = 100
    u = u3

    fig3 = plt.figure(3)
    ax3 = run_simulation(z_0, T, u)
    plt.title("Map of Path Q3 - Amplitude inc.")

    # Question 3: Frequency increase
    z_0 = np.array([0,0,0,0], dtype=np.float64)
    T = 100
    u = u4

    fig4 = plt.figure(4)
    ax4 = run_simulation(z_0, T, u)
    plt.title("Map of Path Q3 - Frequency inc.")

    # Question 3: Amplitude and Frequency increase
    z_0 = np.array([0,0,0,0], dtype=np.float64)
    T = 100
    u = u5

    fig5 = plt.figure(5)
    ax5 = run_simulation(z_0, T, u)
    plt.title("Map of Path Q3 - Amp. & Freq. inc.")

    plt.show()
    # plt.savefig('Question 1.png')