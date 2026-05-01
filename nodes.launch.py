import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69eb7541650da4466a52de5a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69eb7541650da4466a52de5a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69eaea6f650da4466a52d3bc","mode":"speed","max_speed":1800,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ed68d1650da4466a52f260","source_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"rear_right_motor","target_pin_id":"command"},{"connection_id":"69ed68d4650da4466a52f2d0","source_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69ed689d650da4466a52f065",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ed689d650da4466a52f065",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69eaea69650da4466a52d346","mode":"speed","max_speed":1800,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ed68f1650da4466a52f340","source_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69ed68a1650da4466a52f12a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ed68a1650da4466a52f12a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69eb7517650da4466a52d9c4","mode":"speed","max_speed":1800,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69f0333d86ddc7307fba4dad","source_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69eda439650da4466a52fa53",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69eda439650da4466a52fa53",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69eb7514650da4466a52d93e","mode":"speed","max_speed":1800,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69f0333b86ddc7307fba4d3d","source_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_n69f033a586ddc7307fba531e",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69f033a586ddc7307fba531e",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"teleop","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e74fcd15153dec61d870:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3e74fcd15153dec61d870:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69f033ac86ddc7307fba53e1","target_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n69ed68a8650da4466a52f19c",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ed68a8650da4466a52f19c",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.095,"wheel_separation":0.24,"max_wheel_speed":1800}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e71bcd15153dec61d7f8:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3e71bcd15153dec61d7f8:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69f033a186ddc7307fba52ac","source_node_id":"69f0339c86ddc7307fba51e9","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69f033ac86ddc7307fba53e1","source_node_id":"69f033a586ddc7307fba531e","source_pin_id":"mode","target_pin_id":"mode"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ed68d1650da4466a52f260","target_node_id":"69eb7541650da4466a52de5a","source_pin_id":"rear_right_motor","target_pin_id":"command"},{"connection_id":"69ed68d4650da4466a52f2d0","target_node_id":"69eb7541650da4466a52de5a","source_pin_id":"rear_right_motor","target_pin_id":"command"},{"connection_id":"69ed68f1650da4466a52f340","target_node_id":"69ed689d650da4466a52f065","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69f0333b86ddc7307fba4d3d","target_node_id":"69eda439650da4466a52fa53","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69f0333d86ddc7307fba4dad","target_node_id":"69ed68a1650da4466a52f12a","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n69f0339c86ddc7307fba51e9",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69f0339c86ddc7307fba51e9",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2,"output_mode":"diff_drive"}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e702cd15153dec61d7da:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3e702cd15153dec61d7da:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3e702cd15153dec61d7da:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69f033a186ddc7307fba52ac","target_node_id":"69ed68a8650da4466a52f19c","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="logger",
            executable="logger_node",
            name="logger_n69f4bd3a907bab700a8c8217",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69f4bd3a907bab700a8c8217",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"log_file":"","log_to_stdout":true}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
    ])