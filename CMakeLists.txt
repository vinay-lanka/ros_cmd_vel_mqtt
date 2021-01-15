cmake_minimum_required(VERSION 3.0.2)
project(cmd_vel_mqtt)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)
catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


catkin_install_python(PROGRAMS
  scripts/cmd_vel_pub_mqtt.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)