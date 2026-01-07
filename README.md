
Cel paczki:

Paczka ma za zadanie dostarczać interfejs do sterowania robotem, jak i zapewniać możliwość sterowania w dwóch kierunkach: do przodu i do tyłu.
Sterowanie odbywa się za pomocą okna podzielonego na dwie części. Kliknięcie górnej części okna przemieszcza robota do przodu przez 2 sekundy, kliknięcie dolnej części okna przemieszcza robota do tyłu przez dwie sekundy.

Instalacja paczki:

By zainstalować paczkę, należy upewnić się, że:
-W głównym katalogu, w każdym terminalu jest zainstalowane środowisko ROS poleceniem:
~source install/setup.bash~
-W terminalu 1 jest wskazana nazwa robota ('export TURTLEBOT3_MODEL=burger') jak i wskazanie modelu robota (export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`ros2 pkg \
prefix turtlebot3_gazebo \
`/share/turtlebot3_gazebo/models/) 
-Robot jest zainstalowany poleceniem 'sudo apt install ros-humble-turtlebot3*'
Po zbudowaniu ('colcon build') należy Postępować zgodnie z poniższymi poleceniami:

Terminal 1 (uruchomienie robota): 
ros2 launch turtlebot3_gazebo empty_world.launch.py

Terminal 2 (Uruchomienie Rviz)
ros2 launch turtlebot3_bringup rviz2.launch.py

Terminal 3 (Uruchomienie interfejsu graficznego):
ros2 run camera_subscriber camera_node

Terminal 4 (uruchomienie możliwości sterowania):
ros2 run camera_subscriber robot_controller
Przygotowane przez Wojciecha Gocałka 15123, oraz Mateusza Matuszewskiego 151006



