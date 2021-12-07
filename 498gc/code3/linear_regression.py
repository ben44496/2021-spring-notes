import numpy as np
import numpy.linalg as la
from geometry_msgs.msg import Point
from sensor_msgs.msg import LaserScan
# from sklearn.linear_model import LinearRegression

# https://stackoverflow.com/questions/52070293/efficient-online-linear-regression-algorithm-in-python
def lr(x_avg,y_avg,Sxy,Sx,n,new_x,new_y):
    """
    x_avg: average of previous x, if no previous sample, set to 0
    y_avg: average of previous y, if no previous sample, set to 0
    Sxy: covariance of previous x and y, if no previous sample, set to 0
    Sx: variance of previous x, if no previous sample, set to 0
    n: number of previous samples
    new_x: new incoming 1-D numpy array x
    new_y: new incoming 1-D numpy array x
    """
    new_n = n + new_x.size

    new_x_avg = (x_avg*n + np.sum(new_x))/new_n
    new_y_avg = (y_avg*n + np.sum(new_y))/new_n

    if n > 0:
        x_star = (x_avg*np.sqrt(n) + new_x_avg*np.sqrt(new_n))/(np.sqrt(n)+np.sqrt(new_n))
        y_star = (y_avg*np.sqrt(n) + new_y_avg*np.sqrt(new_n))/(np.sqrt(n)+np.sqrt(new_n))
    elif n == 0:
        x_star = new_x_avg
        y_star = new_y_avg
    else:
        raise ValueError

    new_Sx = Sx + np.sum((new_x-x_star)**2)
    new_Sxy = Sxy + np.sum((new_x-x_star).reshape(-1) * (new_y-y_star).reshape(-1))

    beta = new_Sxy/new_Sx
    alpha = new_y_avg - beta * new_x_avg
    # return new_Sxy, new_Sx, new_n, alpha, beta, new_x_avg, new_y_avg
    return new_x_avg, new_y_avg, new_Sxy, new_Sx, new_n, alpha, beta # alpha + beta*x + epsilon

def preprocess(laser_scan):
    """
    lidar_points: sensor_msg/LaserScan type rosmsg
    range_min: float32
    range_max: float32
    """
    lidar_points = laser_scan.ranges
    range_min = laser_scan.range_min
    range_max = laser_scan.range_max
    angle_min = laser_scan.angle_min
    angle_max = laser_scan.angle_max

    point_cloud = np.array(lidar_points)
    center = (range_max + range_min)/2
    r = (range_max - range_min)/2
    point_cloud = np.where(abs(point_cloud - center) <= r, point_cloud, 0)
    return cart_from_polar_arr(point_cloud, angle_min, angle_max)


def cart_from_polar_arr(lidar_points, angle_min, angle_max):
    lidar_points = np.array(lidar_points)
    n = lidar_points.shape[0]
    polar_coords = np.zeros((n, 2)) # (r, theta)
    polar_coords[:,0] = lidar_points
    polar_coords[:,1] = np.linspace(angle_min, angle_max, n)

    return np.apply_along_axis(cart_from_polar, axis=1, arr=polar_coords)

def cart_from_polar(coord): # (r, theta), rad
    r = coord[0]
    t = coord[1]
    return r*np.cos(t), r*np.sin(t)


def incremental_model(points, threshold=0.05, min_points=4, dead_radius=0):
    n = points.shape[0]
    model = lr(0, 0, 0, 0, 0, points[:2, 0], points[:2, 1])
    start_index = 0
    endpoints_list = list()
    i = 2
    while i < n:
        x, y = points[i, :]
        if x**2 + y**2 <= dead_radius:
            i += 1
            continue

        y_hat = model[-2] + model[-1]*x
        if i != n-1 and abs(y_hat - y) <= threshold:
            model = lr(model[0], model[1], model[2], model[3], model[4], x, y)
        else:
            x_start = points[start_index, 0]
            x_end = points[i-1, 0]
            y_start = model[-2] + model[-1]*x_start
            y_end = model[-2] + model[-1]*x_end
            # endpoints_list.append(np.array([x_start, y_start]))
            # endpoints_list.append(np.array([x_end, y_end]))
            if model[4] > min_points:
                endpoints_list.append(Point(x_start, y_start, 0))
                endpoints_list.append(Point(x_end, y_end, 0))

            model = lr(0, 0, 0, 0, 0, points[i:i+2, 0], points[i:i+2, 1])

            start_index = i
            i += 1
        
        i += 1
    return np.array(endpoints_list)



#  def incremental_model(points, threshold=0.05, N=2):
#     n = points.shape[0]
#     model = lr(0, 0, 0, 0, 0, points[:2, 0], points[:2, 1])
#     start_index = 0
#     endpoints_list = list()
#     i = 2
#     while i < n:
#         x, y = points[i, :]
#         if x == 0 and y == 0:
#             i += 1
#             continue

#         y_hat = model[-2] + model[-1]*x
#         if i != n-1 and abs(y_hat - y) <= threshold:
#             model = lr(model[0], model[1], model[2], model[3], model[4], x, y)
#         else:
#             x_start = points[start_index, 0]
#             x_end = points[i-1, 0]
#             y_start = model[-2] + model[-1]*x_start
#             y_end = model[-2] + model[-1]*x_end
#             # endpoints_list.append(Point(x_start, y_start, 0))
#             # endpoints_list.append(Point(x_end, y_end, 0))
#             endpoints_list.append(np.array([x_start, y_start]))
#             endpoints_list.append(np.array([x_end, y_end]))

#             model = lr(0, 0, 0, 0, 0, points[i:i+2, 0], points[i:i+2, 1])

#             start_index = i
#             i += 1
        
#         i += 1
#     return np.array(endpoints_list)



# def fit_lines(points, threshold=1, skip=1):
#     n = points.shape[0]
#     endpoints_list = list()
#     start_index = 0
#     model = lr(0, 0, 0, 0, 0, points[0, :2], points[1, :2])
#     for i in range(2, n, skip):
#         x, y = points[i, :]
#         if x == 0 and y == 0:
#             continue
#         y_hat = model[-2] + model[-1]*x
#         # if la.norm(y_hat - y, 2) <= threshold and i != n-1:
#         if np.sqrt(y_hat**2 - y**2) <= threshold and i != n-1:
#             model = lr(model[0], model[1], model[2], model[3], 1, x, y)
#         else:
#             x_start = points[start_index, 0]
#             x_end = points[i-1, 0]
#             y_hat_start = model[-2] + model[-1]*x_start
#             y_hat_end = model[-2] + model[-1]*x_end

#             endpoints_list.append(Point(x_start, y_hat_start, 0))
#             endpoints_list.append(Point(x_end, y_hat_end, 0))

#             start_index = i
    
#     return endpoints_list





# def fit_line(points, batch_size=4, threshold=1):
#     n = points.size
#     model = lr(0, 0, 0, 0, 0, points[0, :batch_size], points[1, :batch_size])
#     for i in range(1, int(n/4)+n%4): # loop through each batch
#         x = points[0, i:i+batch_size]
#         y = points[0, i:i+batch_size]
#         y_hat = model[-2]*x + model[-1] # alpha + beta*x
#         e = y_hat - y
#         if la.norm(e, 2) < threshold:
#             lr(model[0], model[1], model[2], model[3], batch_size, x, y)
#         else:
#             ...
#             model = lr(0, 0, 0, 0, 0, x, y)