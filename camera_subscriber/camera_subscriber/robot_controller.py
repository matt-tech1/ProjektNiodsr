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
        self.speed = 0.25
        self.motion_duration = 2.0

        self.stop_timer = None

    def point_callback(self, msg):
        twist = Twist()

        if msg.y < self.image_height / 2:
            twist.linear.x = self.speed
            state = 'FORWARD'
        else:
            twist.linear.x = -self.speed
            state = 'BACKWARD'

        self.cmd_pub.publish(twist)
        self.get_logger().info(f'Movement: {state}')

        if self.stop_timer is not None:
            self.stop_timer.cancel()

        self.stop_timer = self.create_timer(
            self.motion_duration,
            self.stop_robot
        )

    def stop_robot(self):
        twist = Twist()
        self.cmd_pub.publish(twist)
        self.get_logger().info('Robot STOP')

        self.stop_timer.cancel()
        self.stop_timer = None


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

