### Announcements
1. Campuswire
2. Website tiny.cc/cs498dv
3. Reading for next week is up

### Today
1. Electromagnetic Waves (Basics)
2. Complex Numbers
3. SNR & Modulation
4. Wireless Channel

#
## EM Waves
Constant Properties:
- Speed: $3 \times 10^8$ m/s (speed of light in vacuum)
- Wave length: distance between consecutive peaks/valleys
- Frequency: cycles per second (Hz)

$c = \lambda f$
- Light: 400Thz or $400\times 10^{12}$
- WiFi: 2.4Ghz/5Ghz, 12cm/6cm wavelength
- 5G: 28Ghz/60Ghz, <1cm wavelength
- 3G/4G: <1Ghz, 30cm

Variable Properties:
- Amplitude (power)
- Phase: Which part of the wave ($\pi/2, \pi$, etc.)

**Question: Can we discuss about how EM waves are affected by atmosphere or boundaries between materials?**

#
## Complex Numbers
$z = a+bj$
$\mathbb{R}^2 =R \times I$
Here, Amplitude is magnitude and phase is angle from x-axis

#### Euler Representation
$\alpha = \sqrt{a^2+b^2}$
$\theta = tan^{-1}(\frac{b}{a})$

**Question: Will we talk about how antenna affects signal?**

Bits ->(Modulation) Complex Numbers -> Antenna -> Wireless Channel -> Antenna -> Complex Numbers ->(Demodulation) -> bits

### Modulations
- On-off keying: Send signal on for bit 1, off for bit 0
- Amplitude Modulation: Depending on amplitude it changes (think square wave at different y-axis). Each unit on y-axis transmits a number in bit
- Phase Modulation:
	- Binary Phase Shift Keying (BPSK): Assign $Real(z) = 1$ as 1 and $Real(z) = -1$ as 0.
	- Quadrature Phase Shift Key (QPSK): (also 8-QPSK)
		- $1+j =$ 00
		- $-1+j =$ 01
		- $-1-1j =$ 11
		- $1-j =$ 10
	- Note: Noise affects FM more because it affects phase and amplitude which is needed for FM.

**Question: Which modulations are good for which applications?**

So what stops us from just increasing resolution to sen dmore bits for AM? Because of **Noise**

### Signal-to-Noise Ratio
Definition: $\frac{Signal Power}{Noise Power}$


**Question: Are we going to talk about Fourier Transforms and FFT in this course?**

#
## Wireless Channel ($h$)
This is the effect the environment creates when a signal goes through it.
What happens if my entire polar equation shifts (translates)?
Channel Equation: $y = hx$ (Note it is a linear equation)
$h$ is a complex number (amplitude usually <1, phase)
$y$ is the received signal (complex)
$x$ is the sent signal (complex)
$h = \frac{y}{x}$, using (euler's?) formula ($ze^{j\theta}$)

You can even try using Wireless Channel to infer stuff about the environment.

### Preamble:
This is a standard that is agreed upon everyone.
I will send x preamble, you receive y preamble, and you use h-estimate to figure out x-preamble to match

**Question: Is this H matrix low dimensional? When, if it isn't, would it be high dimensional?**
**Question: What happens to h-estimate if I keep moving after I have established my preamble?**
