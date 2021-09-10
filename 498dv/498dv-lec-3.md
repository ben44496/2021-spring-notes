- 1 Reading Assignments (down to 1 per week)
- Problem sets: MatLab vs. Python
- Project ideas & resources

Project idea: Wireless indoor localization via Multipath (MIMO?); Drone shouting and trying to find it utilizing interference

#
### Recap Wireless Channel
Tx ($x$)-> Rx ($y$)
$y = hx$ where $x,y$ are complex numbers and $h$ is the wireless channel

Send a preamble message that is globally known

#
## Multiple Input Multiple Output (MIMO)

### SNR / Diversity Beamforming / Diversity Gain
Real equation: $y = hx + n$ where $n$ is noise
- Could be temperature based for example (radiation)

SNR = $\frac{\text{Signal power}}{\text{Noise Power}} = \frac{(hx)^2}{n^2}$
dB$_{log_{10}}$ = $10 log_{10}(\frac{(hx)^2}{n^2})$

One transmitter to two receivers:
$y_1 = h_1x+n_1$
$y_2 = h_2x+n_2$
$y_1+y_2 = (h_1+h_2)x+(n_1+n_2)$
Assuming $|h_1|=|h_2|$ and $|n_1|=|n_2|$

If they are aligned, they magnify amplitude/gain, but if they are opposite direction they cancel each other out

SNR = $\frac{|(h_1+h_2)x|^2}{|n_1+n_2|^2} = \frac{|\sqrt{2}h_1x|^2}{|\sqrt{2}n_1|^2} = \frac{|h_1x|^2}{|n_1|^2}$

**Conclusion**: So as you can see, there is no additional benefit to adding more antennas, just additional gain

**Please copy the proof of the next part from the online notes to show 2 SNR**

**Conclusion**: There is a multiplying factor we can combine in a smart way so we can double SNR

**Please copy the proof of the next part from the online notes to show there is some $\alpha$ we can use to show we can boost SNR**

$\alpha = \frac{h_1}{h_2}$

This is called **Diversity Beamforming** or **Diversity Gain**

$\text{SNR} \leftrightarrow \text{datarate}$
$\text{datarate} \propto log(\text{SNR})$

Therefore increasing SNR is only helpful if you have shitty SNR in the first place.

***
### MIMO

2x2 system-
$y_1 = h_{11}x_1+h_{21}x_2+n_1$
$y_2 = h_{12}x_1+h_{12}x_2+n_2$
$y = Hx + n$
$H^{-1}y = x + H^{-1}n$ - This is called **Multiplexing**, basically it increases our data rate because it allows us to send two messages at the same time

#### Benefits of MIMO
- Manage interferences
- Get multiple streams
- Lets you operate in low SNR conditions

#
### Paper
#### Antenna-Spatial Representation
Example: 2x2
Axis are $y$s and the vector is $x$, where the coordinte is $(h_{12},h_{11})$

<!-- We can decrypt to messages by dot product one of the vectors with the perpindicular of the other vector. -->

**Please copy some h perpindicular proof from online please thank you**

So you can either send the same signal increase SNR and send different signal to increase throughput



#### Stephonic Gil (Robotics + Sensing)
