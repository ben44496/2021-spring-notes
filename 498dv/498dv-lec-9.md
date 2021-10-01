## Supervised ML

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