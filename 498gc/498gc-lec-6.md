## Euler Angles

**Pose** - Position + Attitude

Euler Angles - $\theta$ pitch, $\phi$ roll, $\psi$ yaw

**Standard sequence of rotations** is going to be $z, y, x$ or $\psi, \theta, \phi$.

**Euler's rotation theorem**: states that in 3-D space, any displacement of a rigid body such that a point ont he rigid body remains fixed, is the equivalent to a single rotation about some axis that runs through the fixed point.

## Complex Numbers
### Trignometric form:
$a + ib = rcos\theta + ibsin\theta$
Where $R = \sqrt{a^2+b^2}$
And $\theta = arctan(\frac{b}{a})$

### Polar form:
$a+ib = re^{i\theta}$
...

Complex Conjugate: $|z|^2 = z\bar{z} = a^2+b^2$
Inverse: $z^{-1} = \frac{\bar{z}}{|z|^2}$

## Quaternions
$q = q_0 + q_1i + q_2j + q_3k$ 
$i^2 = j^2 = k^2 = ijk = -1$

### Quaternion Multiplication
- Skew-Symmetric matrix A^T = -A (hence diagonal of A must be zero)
** RIGHT DOWN THE SKEW SYMMETRIC MATRIX FOR MULTIPLICATION **
....
$q^{-1} = \frac{q^*}{||q||^2}$

So we have axis of rotation and scalar part is degree of rotation. 

We have rank 4 but we need to operate on rank 3 so we do:
$v \rightarrow 0 + \bar{v}$
This is what we call a **Pure Quarternion**.

### Triple Product
- Recall for copmlex numbers multiplication by the conjugate results in a real number
- For quaternions, we have the triple product. If $v = 0 + \bar{v}$ is a pure quarternion, then
$\bar{w_1} = q\bar{v}q^*$
$\bar{w_2} = q^*\bar{v}q$

### Relating quaternion to angles
$||q||_2 = 1 = cos^2\theta + sin^2\theta$
$||q||_2^2 = |q_0|^2 + ||\bar{q}||^2 = 1$

... Please write this slide and the next one as well.

Quaternion Rotation Theorem:
For any unit quarternion $q = q_0 + \bar{q} = cos\theta + \bar{u}sin\theta$ and any vector $v \in \mathbb{R}^3$...

The Quarternion Rotation Sequence ...

#
# Lab 2: ROS
```py
import rospy
from std_msgs.msg import Int32

class PublisherNode():

	def __init__(self):
		self.loop_hertz = 10.0 # Update frequency
		
	def run(self):
		self.rate = rospy.Rate(self.loop_hertz) # This line is used to declare the time loop
		pub = rospy.Publisher('publisher_node_example', Int32, queue_size=1)
		A = 0
		while not rospy.is_shutdown():
			pub.publish(A)
			A += 1
			print(A)
			self.rate.sleep()
			
if __name__ == '__main__':
	# Initialize the node and name it
	rospy.init_node('rospy_publisher', anonymous = True)
	ne = PublisherNode()
	ne.run()
```

```py
import rospy
from std_msgs.msg import Int32

class listernerNode():

	number = 0.0
	A = 0.0
	
	def __init__(self):
		self.loop_hertz = 10.0
		
	def run(self):
		self.rate = rospy.Rate(self.loop_hertz)
		rospy.Subscriber(...)
```