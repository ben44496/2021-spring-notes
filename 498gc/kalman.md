
The kalman filter will return a mean (average) of the quantity being estimated and provide a predictive variance on its estimate given:
* The process and measurement noise variance is known
* The dynamical system model is known

The Kalman filter is guaranteed to be the optimal un-biased estimator for the following case:
* The noise in the sensors is Gaussian
* The dynamical system is linear
* Sufficient number of states of the dynamical system are measured (the system is *observable*)

## Noisy continuous-time Linear and Time-Invariant (LTI) systems
$\dot{x} = Ax + B\omega_t$

$y = Hx + v_t$

## Noisy discete-time systems
$x_{k+1} = \Phi_k x_k + \Gamma_k \omega_k$

$y_k = H_kx_k+v_k$

In particular, $\Phi_k = e^{A\Delta t}$, $\Gamma_x = B(t)\Delta t$, $H_k = C(t)$ where $\Delta t$ is the sampling time $dt$.

## Noise Properties
### Additive process and measurement noise
The zero-mean additive Gaussian white noise assumption

$w_k \sim \mathbb{N}(0, Q_k)$: The process noise, encodes the uncertainty in the sensors

$v_k \sim \mathbb{N}(0, R_k)$: The measurement noise, encodes our uncertainty in modeling the process

- The measurement noise $R_k$ (typically stationary: $R$) is typically provided in the sensor specification sheets, its the variance of the sensor
- $Q_k$ (or when stationary: $Q$) is a little more difficult to find, typically this is the variable that needs to be *tuned*

## Q and R matrices
We assume:
- Zero mean, uncorrelated (ie. $\omega_k \sim \mathbb{N}(0, \sigma^2_{\omega}), v_k \sim \mathbb{N}(0, \sigma^2_{v})$)
- $E[(\omega_t, \omega_s)] = Q\delta(t-s)$, $E[(v_t, v_s)] = R\delta(t-s)$, where $\delta$ is the dirac delta function, s.t. $\delta(t-s) = 1$ when $t=s$
- no cross correlation between $w_k$ and $v_k$ (ie. $cov(w_k, v_k) = 0$ for all k)

Herein lies the "official" definition of Process and Measurement noise. What it is saying is that you can set the diagonal term as $\sigma_{\omega}^2$ and $\sigma_v^2$
- **Practically**, $Q$ matrix represents the confidence in the process model, larger the $Q$ matrix, the less confident we are
- **Practically**, $R$ matrix represents the confidence in the measurements from the correcting sensors, higher the $R$ matrix, the less confident in the measurements we are

# Kalman Filter
1. **Prediction**: This is the a-priori stage, that is before the measurement is available, or in between any two measurements. We will denote all variables in this stage with a $-$ sign (e.g. $P^{-}$, $\hat{x}^{-}$)
2. **Correction**: This is the prosteriori stage, that is after the measurement is available. We will denote all variables in this stage with a $+$ sign (e.g. $P^{+}$, $\hat{x}^{+}$)

### Kalman Equations
$E[x_{k+1}] = \Phi_kE[x_k] + 0$

Let $\mu_k = E[x_k]$

The covariance matrix: $P_k = E[(x_k - \mu_k)(x_k-\mu_k)^T]$ 

#### **Prediction**:
$x_k^- = \Phi_kx_{k-1}$

$P_k^- = \Phi_kP_{k-1}\Phi_k^T + Q_k$

#### **Correction**:
$e_k = y_k - H_kx_k^-$

$S_k = H_kP_k^-H_k^T+R_k$

$L_k = P_k^-H_k^TS_k^{-1}$

$x_k^+ = x_k^- + L_ke_k$

$P_k^+ = P_k^- - L_kS_kL_k^T$



### Kalman Gain:
The measurements' certainty-grading and current-state estimate are important considerations. It is common to discuss the filter's response in terms of the Kalman filter's gain. The Kalman-gain is the weight given to the measurements and current-state estimate, and can be "tuned" to achieve a particular performance.

#### Optimal gain $L_k$
To compute the optimal gain $L_k$ we minimize $trace(P_k^+)$ w.r.t. $L_k$. To do this, solve $\frac{\delta trace(P_k^+)}{\delta L_k} = 0$ for $L_k$.














