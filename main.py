# This is main script for Toy Robot.
import configparser
import logging
from robot.robot import Robot
import re


class Process:
    @classmethod
    def start(cls, cmd_file, log_path, log_level):
        # set log message format
        logging.basicConfig(filename=log_path,
                            format='%(asctime)s - %(name)s -  %(funcName)s() - %(levelname)s - %(message)s',
                            level=log_level)
        # logger for this main script
        logger = logging.getLogger('main')

        logger.info('Start')
        # reading command file
        robot_obj = Robot(0, 5, 0, 5)
        try:
            logger.debug('Reading command file {}......'.format(cmd_file))
            input_file = open(cmd_file, 'r')
            contents = input_file.read()

            # process input file
            logger.debug('Processing commands......')
            commands = []
            for line in contents.splitlines():
                # support case in sensitive
                # split command line into command and parameters
                commands.append((line.upper().strip()).split(' ', 1))

            # execute commands
            logger.debug('Executing commands......')

            # TODO: add command parsing function in Robot class
            # TODO: using fuzzy logic to allow typo error in command line
            for command in commands:
                if command[0] == Robot.CMD_PLACE:
                    # valid PLACE command: "[x position],[y position],[facing]", but allow spaces
                    if re.match(r"\s*[0-9]\s*,\s*[0-9]\s*,\s*[A-Z]", command[1]):
                        # remove all spaces
                        place_para = command[1].replace(' ', '').split(',')
                        robot_obj.place(int(place_para[0]), int(place_para[1]), place_para[2])
                elif command[0] == Robot.CMD_MOVE:
                    robot_obj.move()
                elif command[0] == Robot.CMD_LEFT:
                    robot_obj.left()
                elif command[0] == Robot.CMD_RIGHT:
                    robot_obj.right()
                elif command[0] == Robot.CMD_REPORT:
                    robot_obj.report()
                else:
                    # unknown command do nothing
                    logger.debug('Unknown Command:{}'.format(command))
        except FileNotFoundError:
            logger.error('Command file not found')

        logger.info('End')
        return robot_obj.get_position()


if __name__ == '__main__':
    try:
        # read from configuration file
        config = configparser.ConfigParser()
        config.read('ConfigFile.properties')
        # get command input file path
        cmd_file = config.get("command_file", "command_file_path")
        # get log file path
        log_file = config.get("log_file", "log_file_path")
        # get log level
        log_level = config.get("log_file", "log_level")
        log_levels = {'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR,
                      }
        # start
        Process.start(cmd_file, log_file, log_levels.get(log_level, logging.ERROR))
    except Exception as ex:
        print('Error occurred:{}'.format(str(ex)))
