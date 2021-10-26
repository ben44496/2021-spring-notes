# CS 498 ML in Networks - 1

TA: Jay Shenoy
deepakv@illinois.edu

tiny.cc/cs498dv
Campuswire for Discussion
Stuff can make up for other stuff, average A

### Lecture
- 5G
	- High bandwidth, Ultra-low latency, Low power IoT devices
- Communication
	- Low Latency, Wide Coverage
- Earth Observation
	- High Res, High revisit rates, Multi-spectral
- Smart cities
- Personalized Healthcare
- Sensing
	- Soil monitoring, climate prediction, crowd analyticsToday:
- Kernal
- Regularization

### Recap: Regression
$x: \mathbb{R}^d$, $y: \mathbb{R}$, $\ell: ||\text{		}||^2$
$f:$ linear functions, $\theta_d$
$f_{\theta}(x) = \theta^Tx$

We want to find $\hat{\theta}$
$\hat{\theta} = argmin_{\theta}\Sigma_{i=0}^{n-1}||f_{\theta}(x_i)-y_i||^2$

We use gradient descent where
$\theta^t = \theta^{t-1} - \alpha\nabla_{\theta}\ell$
Where $\alpha$ is the learning rate.

But this is only linear, ideally we want to learn more complex functions.
Instead of doing regression on $x$, we can do regression on $\phi(x)$, where $\phi$ is some feature set (and any dimensional)

## Kernals
We can think of $\phi$ as literally any combination of functions
ie. $[x, x^2, x^3,...,x^k]$, $[x, log(x), e^x, ...]$

We can take dimensionality of $\phi$ denoted as $K$ where $K\rightarrow \infty$, but how do we map something to infinite dimensional space?

### Matrix Formulation
Consider $y = \theta^Tx$
where $y$ has dimension $n\times1$, $x$ has dimension $n\times d$, and $\theta$ has dimension $1\times d$

$\ell = ||\hat{x}_{n\times d}\theta^T_{d\times 1} - \hat{y}_{n\times 1}||^2$

And we can solve using least squares.
$\theta = (\hat{x}^Tx)^{-1}\hat{x}^T\hat{y} = \hat{x}^T(\hat{x}^Tx)^{-1}\hat{y}$

Question: Why can we just flip $X^T$ to be on the other side?

$\theta = \hat{x}^TC_{n\times1}$ where $C = (\hat{x}^Tx)^{-1}\hat{y}$

$f(x) = \theta^Tx = (\Sigma C_ix_i)^Tx_{d\times 1}$

**... Copy paste some proof here from the lecture notes please**

**Something something kernals**

In order to make sure it is invertible, we can add some "noise" similar to naive bayes' **laplace constant** such that

$\theta = \hat{x}^T(\hat{x}x+\lambda I)\hat{y}$
Where $\lambda \in \mathbb{R^+}$

### Regularization
$\ell = ||\theta^Tx - y||^2$
Think:
We could have a line fit a point, or we can have some n-dimensional polynomial (an infinite number of them in fact) that fits the point.

We like simpler models though, so we instead do:
$\ell = ||\theta^Tx - y||^2 + \lambda ||\theta^T||^2$ and minimize the 2-norm of the theta as well.

The idea of regularization is to reduce overfit.

#### 2-norm vs. 1-norm regularization
1-norm:
- promotes sparsity, aka some values of $\theta$ will be 0
	- Yeah it actually like promotes zero
- If we know a lot of weights will be sparse, we can use the 1-norm

2-norm:
- Simpler functions,
- Not necessarily sparse

0-norm is defined as number of non-zero values of $\theta$. Since 0-norm is non-differentiable, we can use the 1-norm to approximate to promote sparsity.


### Under-fitting vs. Overfitting
Underfitting - Fit a function less complex than our distribution
Overfitting - Fit a function more complex than the true distribution

How do we know if we're underfitting or overfitting? We look at training loss and test loss

We get Training loss continually goes down, but after some point (aka num of batches), the test loss will go from decreasing to increasing.

Tools:
- Regularization (minimize 2-norm, 1-norm)
- Early Stopping

Question: Can't I do optimization on the Test (think euler's whatever)? Is this adaptive learning rate?

Question: What is the difference of using 1-norm to promote sparsity and trimming?
Answer: Basically the same, as the 1-norm promotes zero. Need to check...

#
Next week:
- Decision Trees
- Neural networksPost/email on CW if we have recommendations for guest speakers.

# Perception
Input: $x \in \mathbb{R}^D$, ie. $x_1, x_2, ..., x_D$
$x_{in}$ where $i$ is the dimension, and $n$ is the training sample
Have $y \in \{-1, 1\}$

We have weights into some node, which we apply a non-linear filter over it.
For example, we can have non-linear function (nlf) where it is the sign of the summation.
$\hat{y} = sgn(\Sigma_iw_ix_i)$

We want loss function to be differentiable, that we can find the gradient.
Misclassification loss: $\hat{y} = y \rightarrow 0$, $\hat{y} \neq y \rightarrow 1$
^ however, it is hard to compute gradient

We can just look at the thing inside the nlf such that $\Sigma_iw_ix_i$ has the same sign as $y$ & it's large, then it's good for me. What that means is that for all samples I missclassifiy, I want to minimize $\Sigma_{n\in\bar{M}}w^Tx_ny_n = \Sigma_ny_n\Sigma_iw_ix_{in}$ (where $M$ is correct classification, and $\bar{M}$ is misclassification). Intuition is we want to bring our perception as close to the boundary as possible.

Perception loss:
loss function, $\ell(w) = \Sigma_{n\in \bar{M}}w^Tx_ny_n$

## Gradient Descent
$\nabla_w\ell(w) = \frac{d\ell(w)}{dw_i} = \frac{d}{dw_i}(\Sigma_nw^Tx_ny_n) = -\Sigma x_{in}y_n$

start: $w^0$
update: $w^{t+1} = w^t-\alpha\nabla_w\ell(w)$, where $\alpha$ is the learning rate

Convergence is guaranteed for this classification problem, but there (we don't think) is not a closed form solution.

## Convergence
Convergence of gradient descent is guaranteed. 

# Neural Networks
We have multiple dimensional input layer $x_1$ to $x_D$, output layer $y_1$ to $y_M$, and hidden layer(s) $z_1$ to $z_h$, connected with linear weights.

Define $w^k_{ij}$ to be from nodes in layer $i$ to $j$. 
$z_i = \Sigma_{i=1}^Dw_{ji}x_i$

We have just have linear functions and non-linearlity, the composition of all these weights will just result in another linear function, so we need a non-linearlity in order to make it useful.

Define $h$ has a non-linear operation, and we will have
$z_i = h(\Sigma_{i=1}^Dw_{ji}x_i)$

## Non-linearities
### Last Layer
#### Classification:
Here, we care about classification, so we can use something like $sgn$, but we can't differentiate it, so we use the $sigmoid$ function instead.

$sigmoid = \sigma(x) = \frac{1}{1+e^{-x}}$

#### Multi-class classification:
Here we want a one-hot encoding for output class, so we want to do something like $max$, but it's non-differentiable, so we use $softmax$ function.

$softmax(y_k) = \frac{e^{y_k}}{\Sigma_{m=1}^{M}(e^{y_m})}$

#### Another popular one, tanh
$tanh(x) = \frac{}{}$ ???

## Gradients
Define $z^{(k)}_{h}$ where $k$ is the $k^{th}$ layer, so $z^{(0)} = x$

$z^{(k)}_j = h(\Sigma_{i=1}^{h^k_{ij}}w^k_{i}z^{k-1}_{i})$
where we set the inside $\Sigma_{i=1}^{h^k_{i}}w^k_{i}z^{k-1}_ij$ as $a_j^k$

$z_L = h(\Sigma_i w^k_{i}z^{k-1}_i)$

For regression, let's have loss function be the L2 norm
$\ell(w) = (y - z^L)^2$

$\nabla_w\ell(w) = 2(y-z_j)(-z_j)$Announcements:
- PSET 2 is out
- Project Ideas are out
- 2 Reading assignments per week

Today:
- Deep Neural Networks
- Convolutional Networks
- ReLu
- Loss Functions
- Training, Dropout, etc.

## What do you mean by deep?
- Anything more than 2 hidden layers is called "deep"
- One way to look at it mathematically is that this is a composition of function where hidden layers ($f_1...f_k$) learn different type of function (ie. log, cos, x^2)
- Depth helps a lot more (models more complex functions)
- Think of each previous layers as crafting our features that we then use for regression/classification

## Why Now?
1. Datasets (large)
2. Compute

## Convolutional Networks
We take a sliding window multiplied from some weights which we call a "Convolution"

We can take strides for our sliding window, but what happens if we move off the cliff?

"Kernal" $\rightarrow$ 2x2 convolution, stride = 1

We could zero-pad on the side and try and ensure that your output/input is the same size. This also ensure that our input and output stay the same size. We could also try and not go off the edge.

## Receptive Fields
The receptive fields of a node is how many input values it depends on. As we go deeper into the convolution, the receptive fields of nodes at that level will increase. 

At the start, we want to learn about edges and features, and then deeper into the network, learn about more complex things like eyebrow, facial shape, etc.

## ReLu
Classification, we can use sigmoid
Multi-class classification, we can use softmax

Using sigmoid for deeper networks is not necessarily good because it has a small gradient unless it's near the middle, so we use the Rectified Linear Unit (ReLU) instead.

ReLU(x):
- $0$ if $x < 0$
- $x$ if $x >= 0$

Problem is it is non-differentiable at 0. It practice, that's fine because it's just one point. 
If you really wanted to avoid this scenario, you can use the Leaky ReLU

Leak ReLU(x):
- $\alpha x$, if $x < 0$
- $x$ if $x > 0$
where $0 < \alpha << 1$

## Loss Functions
"Cross-Entropy Loss"
Entropy: $H(x) = -\sum p(X=x)log p(X=x)$

Head: $-p(logp)$
Tail: $-(1-p) log(1-p)$

Cross-entropy loss: $-\sum t_i(logp_i)$
$t_i$ is the "ground truth", target/output
$p_i$ is the predicted probability of outcome

Example:
$t_0, t_1 = (0.3, 0.7)$
$p_0, p_1 = (0.2, 0.8)$

## Regularization
$\ell(w)$ in the past we use mean square error (regression), or cross-entropy loss

We can use L2 and L1 norm regularization, where L2 promotes more "smoother" boundaries and the L1 norm promotes sparsity. 

Reminder: L0 norm counts number of non zero functions, L1 is an approximation to L0 norm, but L0 is highly non convex, so we use L1.

Gradient descent is iterative. We can also try early-stopping, which has the same type of regularization effect as L2-norm (think prevent overfitting). 

## Learning Rates

## VGG

## Dropout
"Decision Trees"
- Bagging: take the average of multiple decision trees as our classifier

How we implement bagging is by removing some edges from the neural network randomly. 

When we train, we divide datasets into minibatches (32/64/128)

The ideas is that if my network depends on one weight it probably is overfitting.

## Channels
Channels is the "3rd" dimension of an image. For an RGB image of size 128, the number of channels is 3 and the dimensionality is 128x128x3.

One of the standard techniques to propagate information is to dercrease 1st and 2nd dimension but increase # of channels. 

## Applications


## ... something about putting on IoT
- Why do we want to run ML models on cheap resources constrained devices?
"low-latency", low-energy, "networking" available
"inexpensive"
"Privacy"

... example case with Arduino Uno

## Options
- Linear Regression
- Decision Trees
	- But can't perform well near curves

## Bonsai: Key IDeas
Idea: Maximum performance given limited input

$y(x) = \sum_k i_k(x)W_k^TZx\circ tanh(\sigma V_k^TZx)$

Reduce input $x$ using PCA to a 5 or 10 dimensional space ($Z$). 

$W$ is the actual weights. $V$ is the weighting of importance.
$I_k$ is whether or not the node is in that path.
$Zx$ is after the PCA so we have around 5-10 dimensions in there
We sum over each node (in the path because of $I_k$)

## Sparse Projections
"Streaming Manner" for $Z$.

Typically, we read from memory, and then we discard if we don't need it anymore. In Python Generators, it's sampling point by point. However Bonsai reads one input and just divides that into it's features. 

Streamin Manner here means think about it like we are trying to add up all the rows of $Z$ and $x$ such that we only store 10 + 10 values??

If your output vector is even smaller, you can fit it into one register to make it even faster. 

## Loss function
Not gonna write it out but it's basically:

Regularization of ($\theta, w, V, Z$) + Some other loss function we talked about
s.t. $||Z||_0 \leq B_Z, ||\Theta||_0 \leq B_{\Theta}$

$B_Z$ and $B_{\Theta}$ are the memory and storage constraints. Note these are using the zero norms. 

## Training Process
Option 1: Train a model without budget constraints, then set the smallest values to "pruning" zero

Announcements:
- Midterm review next week
- Midterm: open book, open notes, can bring laptops, no browsers/internet

## Network Architecture Search
How do we save memory in terms of training on resources constrained?

**Input**: $1024 \times 2048$
We can downsample to $256 \times 128$

**Conv. Layer**:
- Num. of output channels
- Kernel size
- Stridelength

Note we have lot of choices for model design.

Naive method: 
- Try all the choices, pick one that works best
- Random sampling
	- Only works well if we have limitations and identify a subset

This is where Network Architecture Search (NAS) comes in.

**Typical:**
Human determines Architecture; Data -> training -> weights
**NAS:**
Data -> search -> architecture; More data -> training -> weights
Human still needs to determines primitives (ie. Convolutional followed by fully connected)

## TinyNAS Paper
Insight: More computation leads to better models

...

## Interpreter vs. Code Generation
1. FLOPs vs. Accuracy
2. Engine vs. Accuracy

Bad engine -> not optimized for tiny devices
Search space for NAS decreases

"Not-optimized"
- Best convolution 5x5
Optimized engine
- "More types of networks"

If we have a choice between optimized engine or not, always better to get optimized engine because it searches in subspace that is known to be good, and can only be as good or better.

Generic Optimized engine
- Conv.
- Fully connected
- LSTM units

## Model Adaptive Memory Scheduling
im2col - Linearlizes convolution such that
$M\times N$ kernal becomes array with size $M*N$
and then each kernal is a row in the matrix so you have a $K\times M*N$ array where $K$ is the number of convolutionsToday:
- Wireless recap
- Autoencoders for PHY
- Modulation Identification

## Modulation
We are trying to transmit a sequence of bits, and we can transmit the bits into an encoding to $x$. For example, this could be BPSK or on-off keying. 

We receive $y$ where $y = hx$ and $h$ is a complex number representing the wireless channel. We defined SNR as $\frac{|hx|}{|n|}$ where $n$ is noise.

## ...
"narrow band" channel $\rightarrow$ ...
"wide band" channel $\rightarrow$ signal is transmitted at multiple frequencies.

WiFi $f$: 2.4 GHz ~$2.4\times10^9$Hz
Bandwidth (aka width of usable space centered around 2.4Hz): 20 MHz
We call these multiple bands we have *subbands* or *subfrequencies*.

How does HW create the signal?
Option 1: I create 64 independent signals at 2.4GHz +- slight variation and add them up
Option 2: Create a signal around a low frequency and then change the frequency. We do something called upconversion where you generate it at a low frequency (because its easier to operate hardware at lower frequencies). For example, we start encoding from maybe 0 to 20MHz, and then when we transmit we then add the 2.4GHz in order to get to high frequency.

Then when the other device receives it, it does the down conversion

## Carrier Phase Offset
Upconvertion (add) $\rightarrow f_{up}$ (large freq)
Downconvertion (down) $\rightarrow f_{down}$

Usually $f_{up} = f_{down}$ but there might be small errors (ie. 2.401 Ghz vs. 2.398 Ghz).
1. If nothing changes in the environment, my signal still changes, because the frequency I'm adding is different than the freuqnecy im subtracting from my signal. The difference in this frequency is called the Carrier Frequency Offset (CFO), and so we end up continuing to add the difference in phase continually. 

Modulation/Coding, Upconversion, Tx
Rx, Downconversion, etc.

## ML vs. Manual
A lot of theory into what a good modulation is.

ML:
- Save human power
- adaptable/end-to-end
- robust/generalizable
- Con- Test set distribution != training

Manual:
- We've already developed pretty good modulation/demod, etc.
- Intepretability
- ...

## Images vs. RF
So how is RF different from Images in terms of ML?
1. Real vs. Complex
2. Sources of noise
	- In images if we are trying to find a cat, noise can be brightness, contrst, resolution, background
	- In RF we have Gaussian noise, multipath, CFO, hardware variation, interference
...

## Autoencoders
$x \rightarrow f(x) \rightarrow$ representation ...
...

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
Today's Lesson
- Interference Alignment and Cancellation
- Rate Adaptation (What data rate, modulation, etc.)
- Medium Access (How to regulate access to WiFi against interference)

#
## Interference Alignment
Example: (2 | 2)x2x2
- Access points are connected through backbone system (ethernet)
- Messages $(x_1, x_2)$, $(x_3, x_3)$
- Receiver $(y_1, y_2)$ to $(y_3, y_4)$

$y_1 = h_{11}x_1 + h_{21}x_2 + (h_{31}+h_{41})x_3$
$y_2 = h_{12}x_1 + h_{22}x_2 + (h_{32}+h_{42})x_3$

We don't have enough variables to get a single solution. Answer: Why not emit $\alpha x_3$ and $\beta x_3$ instead (ie. Transmit ($\alpha x_3, \beta x_3$))?

$y_1 = h_{11}x_1 + h_{21}x_2 + (\alpha h_{31}+\beta h_{41})x_3$
$y_2 = h_{12}x_1 + h_{22}x_2 + (\alpha h_{32}+\beta h_{42})x_3$
***
Interference alignment: 
Choose $\alpha$ and $\beta$ s.t. 
$\alpha h_{31} + \beta h_{41} = h_{21}$
$\alpha h_{32} + \beta h_{42} = h_{22}$
Note: two variables, so singular solution

$y_1 = h_{11}x_1 + h_{21}(x_2+x_3)$
$y_2 = h_{12}x_1 + h_{22}(x_2+x_3)$
Note: $(x_2+x_3) = x'$, something that we don't really care about.

We can solve for $x_1$
***
Interference cancellation:
$y_1 = h_{13}x_1 + h_{23}x_2 + (\alpha h_{33} + \beta h_{43})x_3$
$y_2 = h_{13}x_1 + h_{23}x_2 +(\alpha h_{33} + \beta h_{43})x_3$
Since we know $x_1$ we just solve for the other two variables.
***
Example: (3 | 3)x2x2
- 4 packets on the uplink
- 3 packets on the downlink
***
#### Key Insights
- $n$ antenna system $\rightarrow$ $n$ packets simultaneously
- Channel $h$ value sharing is expensive "overhead"
- Information sharing (bits sharing) can improve interference management

#
## Rate adaptation
- Binary Phase Shift Keying (BPSK), Quadrature PSK, 16 Quadrature Amplitude Modulation (QAM-16, 4bits per symbol)
	- All about SNR
- For lower SNR, BPSK does better (1mbps @ 7dB) versus 16-QAM (0mbps @ 7dB), but at 25 dB we have (1mbps vs. 4mbps) so how do we adapt?

**Question**: Do I just get Least Sig. Bit if I have low SNR?
**Answer**: We get the same datarate as a lower one, so like sure but I guess

How do I figure out what rate should I transmit at?
1. If I transmit & experience loss, go lower
	1. lack of "ack", there are 3 tries
2. When do I go up? Just try once in a while
	1. Exploration vs. Exploitation tradeoff (ie. 9:1 times)

**Note**: RL could optimize this better hmmmm

#
## Medium Access Control (MAC)
How do we regulate access to broadcast medium? It's not like devices can "raise their hands".

**"Polling"-based method**
- Works well when everyone has something to say (through selective choosing)

**ALOHA**
- Everytime someone has something to say, just say it
- If there is a collision you wait for a random amount of time
- Works well if very few people have to say (low probability of collision) and inefficient at high numbers
- Too easy to jam, unfair to those who don't have a lot to say (if someone keeps speaking no one can speak)

**Slotted ALOHA**
- Time is divided in chunks, pick a random slot and speak from beginning to end
- If collision, skip random number of slots

**CSMA** - "listen before you speak"
- Carrier Sense, Multiple Access
- Contention Window: If collision = 2$\times$max, else $2$ for interval 
- This could cause high latency when our max number to wait is very high

"Listen-before-speak" approach:
What happens if the two listeners don't hear so you still get interference at terminal? "Hidden terminal"
If this happens, we use **Request to Send (RTS)**, clear to send (CTS), Message

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

If devices can hear each other, then it wil pass through $n$ intermediaries, thus making the capacity $\frac{1}{n}$, Announcements;
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

No real world thing right now for wireless sensing/mapping.Today (9/16/2021):
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

*We could feed FFT and the 2D mapping of the enviroment given phase and amplitude and chart out a room. Think maybe LiDar but using WiFi (point-based, maybe dataset off LiDar/stereo camera?, unsupervised learning, monte carlo simulation). Wait isn't this just WiFi SLAM?*## Supervised ML

$x \rightarrow f \rightarrow y$
How do we get an estimate $f$ given examples of $x,y$. We need to find $\hat{f}$.

Training Phase - $(x,y) \rightarrow \hat{f}$
Runtime/Test phase - $x_{new} \rightarrow \hat{f} \rightarrow y_{new}$

### The Learning Problem
$(x\times y, p)$
Loss function $\ell$: $y\times y \rightarrow [0, \infty)$

Problem:
$\text{min}_{f:x\rightarrow y}$, $E_{xy}[\ell(f(x), y)]$

**Input Space:**
We want to make sure our input is turned into something "nice" (ie. matrix form, word2vec, RGB), something a machine can understand.

**Output Space:**
Regression: $y \in \mathbb{R}$
Multi-variate Regression: $y \in \mathbb{R}^d$
Classification: $y \in \{-1, 1\}$ (yes or no)
Multi-class classification: $y \in \{0, ..., d\}$
Image: $y \in \mathbb{R}\times\mathbb{R}$
Multi-label classification: $y \in \{-1, 1\}^d$ 

### Probability Distribution ($p$)
$p(x,y)$ - how often we will see $(x,y)$ in data
$p(x,y) = p(y|x) p(x)$
$p(x)$ - how likely a given input is (if I have more cats/dogs, it'll skew towards this rather than like elephant)

Regression:
$p(y|x) = f(x) + \epsilon$, where $\epsilon$ is noise
Classification:
$p(1|x)$ or $p(-1|x)$

### Loss function ($\ell$)
$\ell: y\times y\rightarrow [0, \infty)$

**Regression:**
$y$ is ground truth
$\hat{y}$ is prediction
Possible loss function:
- $||y-\hat{y}||^2$ (aka mean squared error)
- Binary Entropy Loss
- 1-norm
- Threshold function (ie. if $|y-\hat{y}|< \epsilon \rightarrow \ell = 0$ else $|y-\hat{y}|$)

**Classification:**
$\hat{y} > 0 \rightarrow 1$
$\hat{y} < 0 \rightarrow -1$

Possible loss function:
- Square Loss ($\ell = y\hat{y}$)
	- Discontinuity @ 0, non-differentiable
- Hinge loss ($max(|1-y\hat{y}|, 0)$)
	- Non-differentiable @ 1
- $\text{L}_2$ loss ($(1-y\hat{y})^2$)
	- Penalizes "very right" predictions
- Log loss ($log(1+e^{y\hat{y}})$)
	- Continuous, differentiable, pretty good

We don't have $p$ or $xy$ ($xy$ refers to all the possible points of data that is part of the dimension) to compute expecation in order to minimize loss. So instead we calculate an empirical loss:

$\Sigma_{i=0}^{N-1}\ell(f(x_i), y_i)$

## Regression
Linear regression
$x \in \mathbb{R}^d$
$y\in \mathbb{R}$

Given: $\{(x_i, y_i)\}^{N-1}_{i=0}$
$y_i = \theta_0 + \theta_1x_i^1 + \theta_2x_i^2+...+\theta_dx_i^d$
^ This is a hyperplane, for $d$ dimensions

Loss function: $|y_i - f(x_)|^2$
Optimize: $\text{min}\Sigma_{i=0}^{N-1}(y_i - f(x_i))^2$
$= \text{min}\Sigma_{i=0}^{N-1}(y_i - \Sigma_{j=0}^{d}\theta_jx_j)^2$, where $x_0 = 1$

## Gradient Descent - solving optimization problems
Prone to local minima in non-convex functions

$\frac{d\ell_i}{d\theta_k} = \frac{d}{d\theta_k}(y_i - \Sigma_j \theta_jx_j)$
$= 2(y-\Sigma_j\theta_jx_j)(-x_k)$

Start: $\theta_k$
Update:
$\theta_k = \theta_k - \alpha(\frac{d\ell_i}{d\theta_k})$

### Batch Gradient Descent
$\theta_k = \theta_k - \alpha\Sigma_ix_i$

### Stochastic Gradient Descent
...
#### Assumptions
1. Training set and test set are from $p$
2. independently identical data (i.i.d.) - aka anything I do now has no bearing on the future