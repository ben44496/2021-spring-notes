## State Space Models

### Spring-Mass-Dampener
$x_1$ is position, $x_2 = \frac{d}{dt}x_1$ is velocity
$\dot{x_1} = x_2$
$\dot{x_2} = -\frac{k}{m}x_1 - \frac{b}{m}x_2+\frac{1}{m}u$

$\dot{x}(t) = ax+bu, x(0) = x_0$
$x(t) = e^{at}x_0 + \int_0^te^{a(t-\tau)}bu(\tau)d\tau$

State Transition Matrix: $e^{At}$ where $A$ is a matrix

**Important**: A Linear Time Invariate (LTI) system is variable if $Re(\lambda_i) < 0$
All of them must have a real part strictly less than 0 to be stable, else it is unstable.

