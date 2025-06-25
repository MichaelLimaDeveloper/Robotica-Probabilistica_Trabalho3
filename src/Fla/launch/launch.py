from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

'''
def generate_launch_description():
    return LaunchDescription([
        # Lançar o Gazebo com o modelo
        ExecuteProcess(
            cmd=[
                'ign', 'gazebo',
                '/home/laelt/27_05_25.ws/src/Fla/Model/building_robot.sdf',
                '--verbose'
            ],
            output='screen'
        ),

'''
def generate_launch_description():
    return LaunchDescription([
        # Lançar o Gazebo com o modelo
        ExecuteProcess(
            cmd=[
                'ign', 'gazebo',
                '/home/laelt/27_05_25.ws/src/Fla/Model/maze_from_matrix.sdf',
                '--verbose'
            ],
            output='screen'
        ),

        # Ponte /cmd_vel (Twist)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
            output='screen'
        ),

        # Ponte /imu
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/imu@sensor_msgs/msg/Imu@ignition.msgs.IMU'],
            output='screen'
        ),
        # --- NOVAS PONTES PARA A CÂMERA RGB ---
        # Ponte para a imagem da câmera
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/camera@sensor_msgs/msg/Image@gz.msgs.Image'],
            output='screen',
            # Este é o namespace do ROS 2, se você precisar.
            name='rgb_camera', 
            # namespace='seu_namespace_aqui' 
        ),
        
        # Ponte para as informações da câmera (calibração, etc.)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'],
            output='screen',
            name='rgb_camera',
            # namespace='seu_namespace_aqui'
        ),
        # # --- FIM DAS NOVAS PONTES ---
])
