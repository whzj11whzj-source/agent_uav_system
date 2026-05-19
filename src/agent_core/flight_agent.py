
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class FlightNode(Node):

    def __init__(self):
        super().__init__('flight_agent_node')

        self.publisher_ = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

    def send_velocity(self, x, y, z):

        msg = Twist()

        msg.linear.x = x
        msg.linear.y = y
        msg.linear.z = z

        self.publisher_.publish(msg)

class FlightAgent:

    def __init__(self):

        rclpy.init()

        self.node = FlightNode()

    def execute(self, task):

        if task['action'] == 'takeoff':
            self.node.send_velocity(0.0, 0.0, 1.0)
            return 'takeoff command sent'

        return 'unknown action'
