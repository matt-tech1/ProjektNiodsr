#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import cv2
import numpy as np


class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')

        self.declare_parameter('square_size', 50)
        self.square_size = self.get_parameter('square_size').value

        self.publisher_ = self.create_publisher(Point, '/point', 10)

        self.window_name = "control_window"
        self.point = None

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

        self.timer = self.create_timer(0.05, self.draw_window)

    def draw_window(self):
        img = np.zeros((512, 700, 3), np.uint8)

        # linia środka
        cv2.line(img, (0, 256), (700, 256), (255, 0, 0), 2)

        if self.point is not None:
            cv2.rectangle(
                img,
                self.point,
                (self.point[0] + self.square_size,
                 self.point[1] + self.square_size),
                (0, 255, 0),
                3
            )

        cv2.imshow(self.window_name, img)
        cv2.waitKey(1)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x, y)

            msg = Point()
            msg.x = float(x)
            msg.y = float(y)
            msg.z = 0.0

            self.publisher_.publish(msg)
            self.get_logger().info(f'Published point: ({x}, {y})')


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()




