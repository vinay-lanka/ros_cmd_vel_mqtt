# ROS cmd_vel MQTT bridge

## Introduction

A ROS package to use any mqtt broker for storing the /cmd_vel topic. Uses the paho_mqtt client package.

This topic can then be used subscribed by any MQTT client.
Useful for resource constrained IoT Robots .


## Setup

**Requires ROS**
(A guide for installation can be found [here](http://wiki.ros.org/ROS/Installation))

### How to build
```
$ cd /path/to/ws/src
$ git clone <this repository>
$ cd ..
$ rosdep install --from-paths src --ignore-src -r -y --reinstall
$ catkin_make
$ source ./devel/setup.sh
```

## Usage

` $ roslaunch cmd_vel_mqtt cmd_vel_pub.launch`

For example you can use this along with the teleop_twist_keyboard package for keyboard control.

` $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`


Work in progress.
