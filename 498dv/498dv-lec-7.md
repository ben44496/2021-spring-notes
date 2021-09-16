Announcements:
- Reading assignents basically full points
- Post in-class notes -> campuswire

## Channel State Information (CSI)
[https://wands.sg/research/wifi/AtherosCSI/](https://wands.sg/research/wifi/AtherosCSI/)
[https://dhalperi.github.io/linux-80211n-csitool/](https://dhalperi.github.io/linux-80211n-csitool/)
Divide up bandwidth up into multiple frequencies and so you get an $N\times N \times k$ matrix for $N$ antennas and $k$ frequencies.

## Antenna Arrays
Compare signal phase from transmitter to get AoA.

## Human Sensing
We assume that humans are dynamic and so we take the time difference for the given h values.

By definition, we have $h$ is $\Sigma h_k$ where $h_k$ is the reflected path over multiple things. We assume that $h_{human}$ is dynamic and the only another one is $h_{direct}$.

We take the time difference so we get $h_1^{t_2} - h_1^{t_1} = h_{1, human}^{t_2} - h_{1,human}^{t_1}$

However, this is a naive assumption as it is power expensive, assumes the human is the only one moving, and assumes that a human is moving. What happens if there is a roomba or if the human is standing still? Consider also the notion of **dynamic reflections**, where the human's signal also reflects over other things.

So the real equation we get is something like this:
$h_1^{t_2} - h_1^{t_1} = h_{1, human}^{t_2} - h_{1,human}^{t_1} + \text{dynamic multipath}$

Filtering:
- Kalman filter
	- Intuition: Humans have a fixed motion speed. They have limited capability in how they can accelerate and decelerate. Limited parameters of motion. So we get a set of observations from our RF sensor $\rightarrow$ estimate a path through those observations. This path can have multiple constraints (ie. velocity, acceleration, permanence)

Cameras?
- Occlusion
- Depth, but can use multiple cameras
- Privacy

Privacy:
- Wireless sensors can sense through walls, so it could violate privacy.

No real world thing right now for wireless sensing/mapping.