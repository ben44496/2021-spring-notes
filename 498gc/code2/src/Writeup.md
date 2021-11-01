# Code Exercise 2 Writeup
## Question 1
Please see implementation located in `src/MAT TEMPLATE/main_template.py`

## Question 2
We shall evaluate the performance and describe what is happening in English.

|      | R = .01 | R = .1 | R = 10/8 | R = Normal |
|:----:| :----: | :--: | :--: | :---: |
| Q = 0.0001Q | #1 | -- | -- | #2 |
| Q = 100Q | -- | -- | -- | #3 |
| Q = Normal | #4 | # 5 | #6 | -- |

### 1:
The covariances of the position, velocities, and quaternions are near 0 almost instantaneously. The position graph did not really change other than that there seems to be more oscillations than usual. The velocity and quaternion graph show huge oscillations around what their values should be. The omega with bias graph shows the same overall graph shape, except now each line is offset from each other by around 3 radians. The Phi, Theta, Psi graph has huge oscillations especially for Psi, and they do not seem at all around what their original values should be. The bias graph also shows bfz having a huge peak and then trending away from the rest, with other lines offset from each other by a lot, seemingly due to some oscillations at the very beginning. The accelerometer and Omega without Bias graph are pretty much the same.

### 2:
The covariance values quickly approach 0 except for some outliers, and in all cases, there seems to be a non-linearity at time stamp ~800 that causes it to spike and then return near back to 0. The position, velocity, and quat graphs both also display a non-linearity around 800, but they seem to be somewhat stable and near their values for the most part. For the Quat graph (fig 6), it oscillates after hitting that non-linearity without regards to its actual value, most likely because it has lost its bearing and has no way of figuring it out. It oscillates around $-\pi$ to $\pi$ radians. The Phi, Theta, Psi graph likewise shows the same thing. The Omega with bias follows the intended value until the non-linearity in which it splits into 3 distinct parts, with q, p, r being at roughly 0, -2, and -5 radians respectively. The bias graph is completely weird after the non-linearity and has the accelerations split off away from the bias of the gyro. Omega without Bias and accelerometer are roughly the same. 

### 3:
Increasing the Q matrix seems to make the quasternions more jagged and rough. This can be seen in both the covariance of quaternions, Quat, and Phi/Theta/Psi graph (fig 3, 6, 8). The Bias graph is also dampened in this instance. The covariance for velocities is way higher than in the normal graph, with the y vel going up above 60. 

### 4:
After the 30 iterations, we receive a matmul overflow and the covariance, position, vel, quat, omega w/ bias, Phi/Theta/Psi, and Bias graphs (fig 1-9) shoot up to near inf. 

### 5:
The graphs for the covariances is best described as consistently overshooting by a small margin and then being followed by a correction. Also to note is that the peaks for these are not that high. The position, velocity, and quat graphs are roughly the same, witht he quat graph having a lot more jagged spikes as it tries to find its actual value. This is then reflected in the Phi/Theta/Psi graph. The bias graph also has notable inconsistencies, with all lines a lot more pronounced in terms of overshoot/undershoot. All other graphs are roughly the same.

### 6: 
There is not much discernable differences between these adn the graphs of the actual values. There are some inconsistencies here and there, but they are soon corrected away. This applies to all graphs.

### Conclusion:
The EKF is seems to be a more sensitive to Q than it is to R (aka robust to R) when comparing changes of the same magnitude. Remember, Q represents the process noise and R represents the measurement noise. The filter is fairly robust to small changes within the same magnitude. However, this is most likely due to the system we are modeling being somewhat linear (at least with respect to some derivatives). In a non-linear modeling function, this may not be the case. In both changes of Q and R, the quaternions were the first to be noticably changing, with it being more jagged and spiky which can be attributed to noise being added in. Furthermore, Q also encodes sort of the "smoothness" of the process itself, and thus, althought you may have higher RMS error overall, it is most likely due to the jagged nature of the filter. The filter is more sensitive to Q because it encodes the non-linearity and other processes that are not modeled, and so these gradually build error with respect to time, whereas the R matrix is mostly the same. 

## Question 3
Setting rgpu to 0 is the same as the raw data for the position and velocity data. It is a little bit different for the Quaternions but not by much. The bias is 0 for everythign except for q (probably a hardcoded offset). The covariance graphs are also worth describing as they seem to be decently different that from before. The covariance of position goes from 7 straight to around 1.3 and hovers there after the first few iterations. The covariance of velocities shoots up to around 1.95 and stays rougly around there for the remainder of its lifetime. For the covariance of quaternions, the graphs have the same shape but the red and blue lines shoot all the way to 450 and 270 respectively. The rest of the graphs are pretty much the same.

By removing the gps offset, there is no difference between the robot's raw data and the actual value as we assume that the gps is the center of gravity for the robot. The position and velocity are fairly robust to a bias but because the gps is physically offset from the center of the robot, any rotational forces will be offset and thus we should see changes when the slope of the gyro changes. Indeed that is the case and explains why although we should be seeing some effect, it is not as pronounced. The EKF is able to accomodate for this in the most part, but we can see that it is somewaht subpar in certain areas like from timestamps 750 to 1000 in Phi/Theta/Psi and Quat corresponding to the red line. This can also be attributed to a loss of observability as we accumulate error with respect to the attitude (aka coordinate base changes). 