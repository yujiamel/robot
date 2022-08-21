# This is main script for Toy Robot.
import logging
import logging.config
from robot.robot import Robot
from fuzzywuzzy import fuzz
import re


class Process:
    @classmethod
    def start(cls, cmd_file):
        # set log message format
        logging.basicConfig(filename='robotexec.log',
                            format='%(asctime)s - %(name)s -  %(funcName)s() - %(levelname)s - %(message)s',
                            level=logging.DEBUG)
        # logger for this main script
        logger = logging.getLogger('main')

        logger.info('Start')
        # Reading command files

        robot_obj = Robot(0, 5, 0, 5)
        try:
            logger.debug('Reading command file {}......'.format(cmd_file))
            input_file = open(cmd_file, 'r')
            contents = input_file.read()

            # Process input file
            logger.debug('Processing commands......')
            commands = []
            for line in contents.splitlines():
                # support case in sensitive
                # split command line into command and parameters
                commands.append((line.upper().strip()).split(' ', 1))

            # execute commands
            logger.debug('Executing commands......')

            for command in commands:
                if command[0] == 'PLACE':
                    # valid PLACE command to follow pattern "[x position],[y position],[facing]", but allow spaces
                    if re.match(r"\s*[0-9]\s*,\s*[0-9]\s*,\s*[A-Z]", command[1]):
                        # remove all spaces
                        place_para = command[1].replace(' ', '').split(',')
                        robot_obj.place(int(place_para[0]), int(place_para[1]), place_para[2])
                elif command[0] == 'MOVE':
                    robot_obj.move()
                elif command[0] == 'LEFT':
                    robot_obj.left()
                elif command[0] == 'RIGHT':
                    robot_obj.right()
                elif command[0] == 'REPORT':
                    robot_obj.report()
                else:
                    # unknown command do nothing
                    logger.debug('Unknown Command:{}'.format(command))

        except FileNotFoundError:
            logger.error('Command file not found')

        logger.info('End')
        return robot_obj.get_position()


if __name__ == '__main__':
    Process.start('../tests/testdata/test1.txt')



