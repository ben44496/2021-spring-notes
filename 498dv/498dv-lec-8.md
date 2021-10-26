Today (9/16/2021):
- FMCW- based sensing demo
- Recap: human sensing
- Measuring distances

## Recap: Human Sensing
$h = h_{direct} + h_{human} + h_{reflectors}$

$h' = h_{direct} + h'_{human} + h_{reflectors}$

$h' - h = h'_{human} - h_{human}$

### Ideas from Prev. Lecture:
- RSSI/Signal strength
	- Weak metric, not super accurate
- Antenna Arrays
	- Look at phase difference

#### Fast Fourier Transform (FFT)
Time domain to frequency domain

## Frequency Modulated Carrier Wave (FMCW)
- Use waveform to mesuare distance
- Benefit: Time and frequency become linearly correlated
	- Hard to measure time, so...
	- By measuring frequency I can measure time to get exact ToF
- Frequency vs. Time
	- Difference with received on x-axis is $\Delta T$
	- Difference with received on y-axis is $\Delta F$
- Needs human to be relatively static

$time = \frac{\Delta F}{slope}$

**FMCW $\leftrightarrow$ Distance**
$\Delta T = \frac{\Delta F}{\frac{B}{T}}$

$T$ is time for the sweep

$dist = c \times \Delta T / 2$

Divide by 2 because two way.

Because there are a lot of reflections depending on the objects (ie. a different time delay line for every single object), we can use FFT to divide up the reflected summation of the frequency shift. We do FFT to isolate each of these frequency shifts. Different frequencies (ie. each peeks from FFT on FMCW output) correspond to objects at different distance.


## Resolution
How close do I have to be to an object in order to still have two peaks?
Resolution - smallest distance I can separate (two peaks instead of one)
Intuitively, the more measurements you perform, the better your resolution (antenna array, bandwidth). If I have half the bandwidth, I will have half the resolution for example. 

$Resolution = \frac{c}{2B}$
$B$ is bandwidth

**Question**: But how about SNR? Higher bandwidth have less SNR?
**Question**: Can't the slope change? ie. think moving object, so you get a slope that changes when it bounces back.

## Multipath: Static
Sometimes, FFT will give us a lot of peaks and we don't know where teh human is. What we can do is successive subtraction and then we should get a clean signal.

However, what happens if we see multiple peaks (for one human)

## Multipath: Dynamic
Assumption: Direct reflection will always be the human. 
Proof: Multipath waves will always take longer because they travel more distance.

## Location
We could draw like 2 ellipse, know which one is front and back, and just pick the front one.

**Question**: Doesn't AoA/Phase-Based do the location well? (We have distance, we have theta, we have polar coordinates)

## Applications
- Games that incorporate environment
- Gesture-based control
- Disaster/Rescue-operation, low visibility
- Elder monitoring

**Question**: Does heat affect radio-wave based imagery?

# Ideas:
**Project Idea #1 – Drone Swarm Localization**
Drone swarms need to function in a variety of spaces, and certain applications mean that agents of the swarm will be separated from the “main swarm” (ie. Path discovery, exploration, no path, coverage, etc.). I would like to develop an algorithm using WiFi to help “lost” drones return to the swarm by following the Angle of Arrival (AoA). This takes advantage of multipath, as we would like this agent to follow the path that goes through a door for example, instead of trying to go through a wall. 

The first stage of this would be looking at 5+ stationary agents grouped together, and have one agent outside of this group and see if we can get the correct heading to the swarm. Following stages would eventually incorporate motion planning as well.

**Project Idea #2 – Wireless Indoor Mapping**, Radio wave based imagery
If drone swarms are deployed in an environment, they should be able to take use of their existing infrastructure (ie. Intra-swarm communication, WiFi connection to AP, broadcast + multipath, etc.) to help map out parts of the environment. Mainly, the use case here is obstacle avoidance and while doing so, could also map a room. 

For this idea, the first stage would have a set of ground mobile nodes and see if they can use dynamic multipath to chart a room’s walls. This would also incorporate an EKF to estimate the likeliness there is a wall, and it will send all the information to a centralized node that will display it in a somewhat point-cloud ish environment on ROSVIZ.

*We could feed FFT and the 2D mapping of the enviroment given phase and amplitude and chart out a room. Think maybe LiDar but using WiFi (point-based, maybe dataset off LiDar/stereo camera?, unsupervised learning, monte carlo simulation). Wait isn't this just WiFi SLAM?*