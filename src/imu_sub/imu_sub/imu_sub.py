import rclpy
from rclpy.node import Node
import numpy as np
import math
from sensor_msgs.msg import Imu


class IMUSub(Node):

    def __init__(self):
        super().__init__('imu_subscriber')
        self.topic = "/oakd/imu/data"
        self.counter = 0
        self.num_msgs = 100
        self.data = []
        self.subscription = self.create_subscription(Imu, self.topic, self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):     
        accel = np.array([msg.linear_acceleration.x, msg.linear_acceleration.z])
        accel = accel / np.sqrt(accel[0]**2 + accel[1]**2)
        print(f"{math.asin(np.dot(accel, np.array([0, -1]))) * 180 / math.pi}", end="\r")


def main(args=None):
    rclpy.init(args=args)
    imu_subscriber = IMUSub()
    rclpy.spin(imu_subscriber)
    imu_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()