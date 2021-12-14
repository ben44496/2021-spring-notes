# Problem 1

https://www.youtube.com/watch?v=_W4ORk255VM

As you can see, the spots where the dots are very close together show that those are walls. When the lines start jumping back and forth like in 0:47 when there's a hallway to the right of the robot shows when there is an open space. 

# Problem 2

https://www.youtube.com/watch?v=SEXVdrubhj8

When you open rviz, please make sure to select "laser" for Fixed Frame option.

Script to run:
`python3 problem2.py`

Topics to visualize:
- /terrasentia/scan
- /ans/lines

# Problem 3

https://www.youtube.com/watch?v=rWXYnBUjxEk

When you open rviz, please make sure to select "odom" for Fixed Frame option

Script to run:
`python3 problem3.py`


Topics to visualize:
- /terrasentia/scan
- /terrasentia/ekf
- /ans/lines

# Problem 4

https://www.youtube.com/watch?v=c2HQW1A4aW4

When you open rviz, please make sure to select "odom" for Fixed Frame option

Script to run:
`python3 problem3.py`
`rosrun gmapping slam_gmapping scan:=/terrasentia/scan`

Topics to visualize:
- /terrasentia/scan
- /terrasentia/ekf
- /ans/lines
- /map

If you do not have gmapping, download in Linux using `sudo apt-get install ros-noetic-gmapping`, substituting `noetic` for your ros distribution (ie. `kinetic`, `melodic`)