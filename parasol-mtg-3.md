Announcement:
- Open source by 15th, tomorrow

# Abstraction in Reinforcement Learning
Notes:
- High level

Spare reward problem in Q-Learning
- Studies general search problems
- DOn't keep track of what explored
- We can add a goal conditioned policy

## Dealing with spare rewards
- Training a goal conditioned policy
  - Hindsight experience replay
  - Hierarchy
- Intrinsic motivation
  - Exploration (reward for rare states)
  - Curiosity (reward for difficult to model states)

## Abstraction as hierarchy
- "intrinsic" reward to transition between abstract states
- Higher level policy uses lower level policy to navigate a space
- Think: RL train on just one action

Benefits:
- De-sparsify rewards through abstraction
- Learned problem structure is explicit
- Divide and Conquer into subproblems (dimensionality reduction)