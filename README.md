# Proyecto-robotica
## Entrega final para el curso de Robótica Industrial.

## Inicialmente debe clonarse el repositorio en el espacio de trabajo

$ roscd; cd ../src

$ git clone https://github.com/IlFernandez/Proyecto-robotica

Construir el proyecto con el catkin_make
$ cd ..
$ catkin_make

Visualización del UR en Gazebo
$ roslaunch ur5_gazebo ur5_cubes.launch

Apilar cubos de manera secuencial, para apreciar cada acción
$ rosrun ur5_gazebo send_joints0.py
$ rosrun ur5_gazebo send_joints1.py
$ rosrun ur5_gazebo send_gripper0.py
$ rosrun ur5_gazebo send_gripper1.py
$ rosrun ur5_gazebo send_joints2.py
$ rosrun ur5_gazebo send_gripper.py
$ rosrun ur5_gazebo send_joints0.py
$ rosrun ur5_gazebo send_joints3.py
$ rosrun ur5_gazebo send_joints4.py
$ rosrun ur5_gazebo send_gripper3.py
$ rosrun ur5_gazebo send_gripper4.py
$ rosrun ur5_gazebo send_gripper5.py
$ rosrun ur5_gazebo send_joints5.py
$ rosrun ur5_gazebo send_gripper.py

Nota: 
-Ejecutar cada nodo y luego terminar la ejecución antes de ejecutar el siguiente (Ctrl + C).
-Darle Play al Gazebo.
