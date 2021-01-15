#!/usr/bin/env python
import rospy
import paho.mqtt.client as mqtt
from geometry_msgs.msg import Twist
import json

client = mqtt.Client()

client.connect("localhost", 1883, 60)

def callback(data):
    x = {
        "linear":
            {
                "x":data.linear.x,
                "y":data.linear.y,
                "z":data.linear.z
            },
        "angular":
            {
                "x":data.angular.x,
                "y":data.angular.y,
                "z":data.angular.z
            }
        }
    rospy.loginfo(x)
    client.publish("ros_mqtt/cmd_vel", json.dumps(x))

def mqtt_bridge():
    rospy.init_node('mqtt_bridge', anonymous=True)

    rospy.Subscriber('/cmd_vel', Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    mqtt_bridge()