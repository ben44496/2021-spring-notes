# Midterm Practice 1 (Machine Learning)
## 1 Machine Learning
### 1.1 Kernals and Regression
#### 1.1.1
Consider a training set consisting of just three data points: 
$$x = 1, y = 1$$
$$x = -1, y = 1$$
$$x = 0, y = 0$$ 

- (a) We want to train a linear regression model that takes $x$ as input and predicts $y$. Can a linear regression model fit this datset?
  - Ans: Cannot fit a linear model
  - My answer: Yes, but higher error and low $r^2$ correlation coefficient
- (b) If not, define a function, $\Phi$, such that a linear regression model that maps $\Phi(x)$ to $y$ will be able to model the relationship accurately.
  - We can choose $\Phi (x) = x^2$, but there are an infinite number of kernals technically. Concise answer is $\Phi (x) = x^2$, but the trivial answer is $\Phi (x) = (x^3, x^2, x, 1)$ for 3 points.

#### 1.1.2
Recal that a kernal, $K(x,x')$, identifies the similarity between two input points $x$ and $x'$. Assume, $x$ and $x'$ are two-dimensional vectors. Let's define a kernal $K$ such that $K(x, x') = x^Tx' + 4(x^Tx')^2$. This kernal is equivalent to computing, $\Phi (x)^T\Phi (x')$. Identify function $\Phi$, i.e. write $\Phi(x)$ as a function of $x_1$ and $x_2$, the two values in the vector $x$. 
- Two ways of specifying a kernal. We can explicitly state $\Phi (x)$ or an implicit representation $K(x, x')$ which is helfpul when $\Phi (x)$ has many dimensions, possibly infinite.
- To answer the questions, we define $x = (x_1, x_2)$ and $x' = (x_1', x_2')$. We just expand the given definition for $K$ to get 
  - $(x_1x_1' + x_2x_2') + 4(x_1x_1' + x_2x_2')^2$
  - $x_1x_1' + x_2x_2' + 4x_1^2x_1'^2 + 4x_2x_2'^2 + 8(x_1x_2)(x_1'x_2')$
- Answer:
  - $\Phi (x) = \{x_1, x_2, 2(x_1)^2, 2(x_2)^2, 2\sqrt{2}x_1x_2\}$
  - $\Phi (x') = \{x_1', x_2', 2(x_1')^2, 2(x_2')^2, 2\sqrt{2}x_1'x_2'\}$

### 1.2 Neural Networks
#### 1.2.1
Loss functions play an important part in the neural network design. What is a good loss function for (a) binary classification, (b) regression, and (c) multi-label classification?
- (a) cross-entropy
- (b) $L_2$ norm, mean-squared error
- (c) cross-entropy

#### 1.2.2
Non-linear activiation functions are crucial to mdern day neural networks. Answer the following questions about the activation functions:
- (a) Why can't we use linear functions as activation functions?
  - A sequence of linear operations is just another linear operation. We can think of this as setting $w = w_1w_2$. This would mean a neural network with no depth.
- (b) Recall, the sigmoid activation function is given by $\sigma (x) = \frac{1}{1+e^{-x}}$ and tanh is given by $tanh(x) = \frac{e^x-e^{-x}}{e^x+e^{-x}}. Show that $tanh(x)$ can be written as a function of $\sigma (x)$ and $\sigma (2x)$. 
  - $tanh(x) = \frac{e^x}{e^x + e^{-x}} - \frac{e^x + e^{-x} - e^x}{e^x + e^{-x}}$
  - $tanh(x) = \sigma (2x) + \frac{e^x}{e^x + e^{-x}} - 1$
  - $tanh(x) = 2\sigma(2x) -1$
  - Using $tanh$ or $\sigma$ will give us an equivalent neural network as the operations for equivlanece are all linear.
- (c) What's the advantage of using the ReLu function over tanh or sigmoid?
  - ReLU is non-differentiable at 0. Advantage is that higher derivative at $>1$, but $tanh$ and $\sigma$ has low derivative at high x-axis. 

# Midterm Practice 2 (Wireless)
### 1.1 Modulation
Recall, modulation is the process of converting bits into symbols (complex numbers). Each symbol is then trasmitted over the air. For the questions below, assume that the symbols per second are constant, i.e. a transmitter transmits a fixed $N$ number of symbols per second. 
- *True/False*. A QPSK modulation achieves a datarate of $4N$ bits pers second. A QPSK modulation achieves a datarate of $4N$ bits per second.
  - **FALSE**. Remember, QPSK sends out 2 bits per symbol and since we send out $N$ symbols per second, we only achieve a $2N$ datarate.
- *True/False*. A BPSK modulation achieves a datarate of $N$ bits per second.
  - **TRUE**. BPSK sends out 1 bits per symbol (-1, 1) and so we send out $N$ symbols per second.
- *True/False*. A higher modulation (e.g. moving from BPSK to QPSK) always ensure a higher datarate
  - **FALSE**. If we have low SNR, we have more errors at higher modulation.

### 1.2 MIMO
1. We are interested in performing $2\times 2$ MIMO over a channel Matrix $H$, measured between a 2-antenna trnasmitter and a 2-antenna receiver. Which of the following channel matrices can support two complex-valued streams for the MIMO transmissions?
- (a)

    $$H = [[\frac{1+j}{\sqrt2}, \frac{-3+3j}{\sqrt2}], [2j, -6]]$$

    We need to check if $H$ is invertible because $H^{-1}y = H^{-1}Hx$. Easy way for $2\times 2$ is check $det(H) \neq 0 \neq ad-bc$. 
- (b) 
  $$H = [[\frac{1+2j}{\sqrt2}, \frac{-2+3j}{\sqrt2}], [1, -3]]$$

- (c)
    $$H = [[\frac{3}{\sqrt2}, \frac{1}{\sqrt2}], [2j, -6]]$$

1. If the channel matrix doesn't allow for two independent streams of data, how can you leverage the multiple antennas on the transmitter and receiver?
  - We can use Beamforming. Beamforming does not require invertability and get imporved SNR. This is where we can multiple $h_2$ by $\alpha = \frac{h_1}{h_2}$.
  - $y_1 = h_1x + h_2x + n$ and $y_b' = h_1x + n$
    - SNR = $\frac{|h_1 + h_2|}{n}$, $SNR_2 = \frac{|h_1|}{n}
    - SNR = $\frac{|h_1 + h_2\times \frac{h_1}{h_2}|}{n} = \frac{|2h_1|}{n}$

### 1.3 Localization
Assume an ideal world where there are no carrier frequency offsets, no clock offsets, and no noise. Hersh has an idea to estimate the distance from an RF transmitter to an RF receiver, both with one antenna each. so they transmit a sinusoidal waveform at frequency $f$ Hz and then computes the phase of the reflected signal. The radio signal travels at $c$ meters per second. Hersh finds that he can make this approach work as long as the distance to the object is less than some value, $D$ meters. What is $D$ in terms of the parameters provided? Explain your answer.

$\phi = \frac{-2\pi d}{\lambda}$

$(-\frac{\lambda\phi}{2\pi} = d) \text{ mod } 2\pi \times\frac{\lambda}{2\pi}$

$d = \frac{-\lambda\phi}{2\pi} \text{ mod } \lambda$, where $\lambda = \frac{c}{f}$

### 1.4 FMCW Localization
Consider WiTrack, the system we learnt about in class. It uses FMCW (Frequency Modulated Carrier Wave) to measure distance to humans. Assume that we redesign WiTrack with 100 MHz of bandwidth (1 MHz = 10^6 Hz). What is the distance resolution that WiTrack can achieve with this bandwidth.
- Resolution = $\frac{c}{2B}$ where $B$ is the bandwidth and $c$ is speed of light
- Answer: $\frac{3\times 10^8}{2\times 100\times 10^6} = 1.5$m