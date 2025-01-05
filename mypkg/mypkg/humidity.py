"""#!/usr/bin/python3
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
       rclpy.spin(node)   """

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class HumidityPublisher(Node):
    def __init__(self):
        super().__init__("humidity")
        self.pub = self.create_publisher(Int16, "tokyo_humidity", 10)
        self.create_timer(1.0, self.cb)

    def cb(self):        
        msg = Int16() 
        msg.data = random.randint(30, 80)     
        self.pub.publish(msg)
        print(f"湿度: {msg.data}%")  # テスト用の出力を追加
       
def main(args=None):
    rclpy.init(args=args)
    node = HumidityPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
