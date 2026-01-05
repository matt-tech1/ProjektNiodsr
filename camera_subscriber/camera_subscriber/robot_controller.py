#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, Twist


class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        self.subscription = self.create_subscription(
            Point,
            '/point',
            self.point_callback,
            10
        )

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.image_height = 512
        self.speed = 0.2

    def point_callback(self, msg):
        twist = Twist()

        if msg.y < self.image_height / 2:
            twist.linear.x = self.speed
            self.get_logger().info('FORWARD')
        else:
            twist.linear.x = -self.speed
            self.get_logger().info('BACKWARD')

        self.cmd_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

