# haru-smart-home

This is a project regarding the social robot "Haru". We are going to extend Haru with an interface to connect to a smart home and therby control the smart home environment via Haru. The main goal is to let Haru create a suitable learning environment by controlling lights and speakers.

## members

We are a group of students of the Stuttgart Media University (Hochschule der Medien Stuttgart).

| Name             | Studies | Student-Mail           |
| ---------------- | ------- | ---------------------- |
| Anton Gerdts     | AM7     | ag164@hdm-stuttgart.de |
| Daniel Koch      | MI7     | dk119@hdm-stuttgart.de |
| Fabio Mangiameli | MI7     | fm083@hdm-stuttgart.de |
| Johannes Nißl   | MI7     | jn033@hdm-stuttgart.de |

## starting home assistant

- ``cd home-assistant``
- ``docker-compose up -d``
- open [Home Assistant](http://localhost:8123)
- log in with following information:
  - username: haru
  - password: haru123


## ros node

1. open terminal and source ros stuff by executing following command ``source ./catkin_ws/devel/setup.bash``
2. execute ``roscore`` to start ros master
3. open another terminal, source as described in step 1 and start learning node server by running ``rosrun haru_smart_home learning_server.py``
4. open another terminal and source as described in step 1. after that you can either run ``rosrun haru_smart_home learning_client.py on`` to start learning mode or `rosrun haru_smart_home learning_client.py off` to stop learning mode
