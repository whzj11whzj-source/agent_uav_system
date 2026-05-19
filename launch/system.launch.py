
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='flight_control',
            executable='flight_controller',
            output='screen'
        )
    ])
