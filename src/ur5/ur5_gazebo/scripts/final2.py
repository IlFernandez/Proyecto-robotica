import subprocess

process1 = subprocess.Popen(['python', '/home/santiago/lab_ws/src/ur5/ur5_gazebo/scripts/send_gripper0.py'])
process2 = subprocess.Popen(['python', '/home/santiago/lab_ws/src/ur5/ur5_gazebo/scripts/send_joints1.py'])
process3 = subprocess.Popen(['python', '/home/santiago/lab_ws/src/ur5/ur5_gazebo/scripts/send_gripper0.py'])
process4 = subprocess.Popen(['python', '/home/santiago/lab_ws/src/ur5/ur5_gazebo/scripts/send_gripper1.py'])
process5 = subprocess.Popen(['python', '/home/santiago/lab_ws/src/ur5/ur5_gazebo/scripts/send_gripper2.py'])
