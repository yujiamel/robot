Toy Robot Code Challenge

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no 
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented 
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, 
however further valid movement commands must still be allowed. 

Commands:
* PLACE X,Y,F
* MOVE
* LEFT
* RIGHT
* REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner.  

MOVE will move the toy robot one unit forward in the direction it is currently facing.
 
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. 

REPORT will announce the X,Y and F of the robot. 

It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The 
application should discard all commands in the sequence until a valid PLACE command has been executed.A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands. 
Any move that would cause the robot to fall must be ignored. 

Commands are input from a file. 

Below codes have been tested in python 3.9 environment: 
1. main.py to run the application:  
   a. update the input commands file path in main.py
   b. update log level if required
   c. run it under project root dirctory using 
      python main.py 
2. robot module contains Robot class 
3. tests folder includes end-to-end testing and unit-test of Robot class
      unit testing:    python -m pytest tests\test_robot.py 
      end-end testing: python -m pytest tests\test_main.py


