
Przygotowane przez Wojciecha Gocałka 151233, oraz Mateusza Matuszewskiego 151006

Cel paczki:

Paczka ma za zadanie dostarczać interfejs do sterowania robotem, jak i zapewniać możliwość sterowania w dwóch kierunkach: do przodu i do tyłu.
Sterowanie odbywa się za pomocą okna podzielonego na dwie części. Kliknięcie górnej części okna przemieszcza robota do przodu przez 2 sekundy, kliknięcie dolnej części okna przemieszcza robota do tyłu przez dwie sekundy.

Instalacja paczki:

By zainstalować paczkę, należy upewnić się, że:
-W głównym katalogu, w każdym terminalu jest zainstalowane środowisko ROS poleceniem:
`source install/setup.bash`
Projekt jest realizowany w czterech terminalach

Terminal 1:
- Instalacja pakietów TurtleBot3:
  - `sudo apt install ros-humble-turtlebot3*`
- Ustawienie ścieżki modeli Gazebo:
  - `export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo/models/`
- Wybór modelu robota:
  - `export TURTLEBOT3_MODEL=burger`
- Uruchamianie środowiska:
`ros2 launch turtlebot3_gazebo empty_world.launch.py`

Terminal 2:

- Uruchomienie Rviz:
`ros2 launch turtlebot3_bringup rviz2.launch.py`

Terminal 3:

 - Uruchomienie interfejsu graficznego:
`ros2 run camera_subscriber camera_node`

Terminal 4:
- Uruchomienie możliwości sterowania:
`ros2 run camera_subscriber robot_controller`
