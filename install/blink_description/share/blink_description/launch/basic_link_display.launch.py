from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os

def generate_launch_description():
    # Ruta absoluta del archivo URDF dentro de la carpeta de descargas
    urdf_path = os.path.join('/home/robousr/Downloads/Robotica-2025-prac1', 
                             'urdf', 'basic_link.urdf')
    
    # Ruta absoluta del archivo de configuración de RVIZ dentro de la carpeta de descargas
    rviz_config_path = os.path.join('/home/robousr/Downloads/Robotica-2025-prac1', 
                                    'rviz', 'basic_link_config.rviz')
    
    # Definición del parámetro de la descripción del robot que utiliza el archivo URDF
    # Se usa el comando 'xacro' para procesar el archivo URDF si es un archivo XACRO
    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    # Ejecución del nodo robot_state_publisher que publica el estado del robot basado en el URDF
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]
    )

    # Ejecución del nodo joint_state_publisher_gui para manipular los estados de las articulaciones
    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    # Ejecución del nodo RVIZ con la configuración especificada en el archivo de RVIZ
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )

    # Retorna la configuración del lanzamiento con los nodos especificados
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])