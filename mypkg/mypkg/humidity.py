#!/usr/bin/python3
#SPDX-FileCopyrightText: 2025 Kazuya Ochiai
#SPDX-License-Identigier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

rclpy.init()
node = Node("humidity")
pub = node.create_publisher(Int16, "tokyo_humidity", 10)


def cb():        
       msg = Int16() 
       msg.data = random.randint(30, 80)     
       pub.publish(msg)
       


def main():
       node.create_timer(1.0, cb)  
       rclpy.spin(node)   

