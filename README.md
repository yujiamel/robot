Toy Robot Code Challenge 
(This code challenge is provided by iress)

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed. 

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

It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.               
Any move that would cause the robot to fall must be ignored.     

Commands are input from a file.             

Below codes have been tested in python 3.9 environment: 
1. ConfigFile.properties is to config command file path, log path and log level:       
   command_file_path = [command file path]               
   log_file_path = [log file path]                 
   log_level = [log level] (e.g.DEBUG, INFO, ERROR, WARNING)        
   
2. main.py is to read the command input file and trigger Robot class object:  
   a. update ConfigFile.properties for command file path, log file path and log level              
   b. run it under the project root dirctory                 
         python main.py             
2. Robot.py is a robot object class under robot module, which handles robot behaviours   
3. tests folder includes end-to-end test cases of main.py and unit-tests of Robot.py            
         unit testing:    python -m pytest tests\test_robot.py       
         end-end testing: python -m pytest tests\test_main.py              
4. testdata under tests folder contains input command testing files
   
