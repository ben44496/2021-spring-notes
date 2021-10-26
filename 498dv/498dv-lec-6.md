Announcements;
- PSET 1 (2 weeks from today)
- Reading Assignment is out
- TA office hours (Wed. 4-5 pm)

Recap:
- GPS (outdoors)
- RSSI
- Fingerprinting

**Question**: Why is fingerprinting called fingerprinting?
Exisiting database of locations with their corresponding fingerprints, and just match up later.

Today:
- Channel Phase
- Angle of Arrival
- Antenna Arrays
#
## Channel Phase
$h = ae^{j\theta}$
$a = \frac{\alpha}{d}$
$\phi = -(\frac{2\pi}{\lambda} \times d)$ mod $2\pi$
Negative sign because the receiver gets the value after the transmitter?? It is just a notation

**Question**: Why negative sign?

$\angle h_2 - \angle  h_1 = -(\frac{2\pi}{\lambda} \times (d_2-d_1))$ mod $2\pi$
$d_1-d_2 = xcos\theta$
But it is still mod $2\pi$, so we set $x$ to be small, where $x = \frac{\lambda}{2}$ so we get:
$\angle h_2 - \angle  h_1 = -(\pi cos\theta)$ mod $2\pi$
$-1 < cos\theta < 1$
$cos\theta = \frac{\angle h_2 - \angle h_1}{\pi}$

**Question**: Noise, error analysis? Shape of Antenna Array?
Answer: So just choose $x \le \frac{\lambda}{2}$
Answer: Shape of Antenna array doesn't matter too much, just ambiguity I guess.

Problems:
- Front or back ambiguity ($cos(\theta) = cos(-\theta)$)
- Multipath
- Assumption: signals are relatively far away

## Array Track
Observations:
1. More antennas on APs
2. AP density is increasing

$\angle h_0 = \frac{-2\pi}{\lambda}d$

$\angle h_1 = \frac{-2\pi}{\lambda}(d+xcos\theta)$

...

$\angle h_1 = \frac{-2\pi}{\lambda}(d+kxcos\theta)$

$\Sigma_{i=0}^{N-1}h_i \rightarrow$ small number
Insight: How can I rotate $h_1$ so that it is perfectly aligned with $h_0$.
$\angle h_1 = \angle h_0 + \frac{2\pi}{\lambda}xcos\theta$

**Please copy the part where he talks about $\theta'$**
$\Sigma_{i=0}^{N-1}

???
$\Sigma |h_i|$

## Resolution
The peak of the "fourier" graph corresponds to how much power comes along that path. This is what we call the **multipath profile**.

You will get a width for every peak.
Width of peak $\propto \frac{1}{N}$, for $N$ antennas

Resolution is better with more antennas.

Problem: If you have two peaks, how do you know which one is ANDP?
Take different measurements. In the context of ArrayTrack, you use different subsets of the antennas to make the measurements. 

Note: Mirrors are also very consistent in reflection.

The more APs you have, the easier it is to find ANDP through calculations.
Antennas provide a little more information than averaging. 

**Rule of Thumb**: $n$ antennas $\rightarrow \frac{180\degree}{n}$ to find the rough width.

**Front vs. Back**
You sort of know where you're looking?

Limitations:
- Antenna Array is Bulky
- Channel Phase, needs to have addtional hardware
- Power
