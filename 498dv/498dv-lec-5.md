Announcements:
- PS1 is out
- TA OH Wed 4 to 5

## Applications of Localization
Applications:
- Amazon Go
- Roomba/ Factory
- Contact Tracing
- Security

Localization resolution can be $(x,y,z)$, room-level, distance b/w individuals, etc.
Technlogy: WiFi, Bluetooth, GPS, cuztomized

Active/Passive:
- You transmit, infrastructure localizes
- GPS

### Outdoor Localization (ie. GPS):
**Time of Flight:**
- $\lambda * t = d$, $\lambda = 3\times10^8\frac{m}{s}$
GPS orbit at MEO orbit (20,000 km), 0.067s or 67ms delay roughly to get to you

**Accuracy Needed?**
1s? $\epsilon$ = $300,000$ km (Bigger than the earth)

1ms? $\epsilon$ = $300$ km (state of Illinois)

1Ms? $\epsilon$ = $0.3$ km or $300$ m (From CSL to Green St.)

1ns? $\epsilon$ = $3$ m. This is what we need.

**Starting Point** (How do I know when the satellite transmitted its signal?):
Problem: 2:20pm on their clock is not the same as 2:20pm on our phone.

$t_1 + offset$

$t_2 + offset$

$t_3 + offset$

$t_4 + offset$

The differences are ok though. So we can calculate $d_2 - d_1$ with high accuracy.

**Problems:**
- Poor accuracy (few meters)
- Power expensive (not on IoT or small drones)
- Cannot work indoors
- Multipath effect

## Indoor Localization
Received Signal Strength (RSS):
$h \propto \frac{1}{d^2}$ measured in dBm

RSS is not a well-conditioned graph ($\delta > \epsilon$ where $\epsilon = f(\delta)$.
Also it sucks because of multipath.

$y = (h_1+h_2+h_3)x$ where each $h$ is a different multipath to the receiver.

Constructive $\rightarrow$ Signal strength is high

Destructive $\rightarrow$ Signal strength is low

## Fingerprinting
Setup: I measure RSSI at a grid of location
Run-time : identify the best match

Think: I sample a bunch of areas for their RSSI and then do NearestNeighbor classification

Pros:
- Robust to Multipath
- Does not need location of AP

Cons:
- Not scalable/ Ground truthing
- Repeat the process if anything changes, it's environment dependent (recalibration)

There is a movement towards phase-based localization (ie. ArrayTrack).
**Question**: Monte-Carlo Localization? Gradient-based Localization?

### Extra: Mesh Networks vs. MIMO & IAC
The core difference between the two networks is the interference pattern.
In Mesh Network, the assumption is devices cannot hear each other (ie. Fragmented sources of interference).

If devices can hear each other, then it wil pass through $n$ intermediaries, thus making the capacity $\frac{1}{n}$, 