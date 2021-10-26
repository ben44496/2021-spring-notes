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
- Binary Phase Shift Keying (BPSK), Quadrature PSK, 16 Quadrature Amplitude Modulation (QAM-16, 4 bits per symbol)
	- All about SNR
- For lower SNR, BPSK does better (1 mbps @ 7dB) versus 16-QAM (0 mbps @ 7dB), but at 25 dB we have (1mbps vs. 4mbps) so how do we adapt?

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

