# This test file is for end-to-end testing
# Input: file path of test files containing all input commands
# Expected result: its final position
import pytest
from main import Process


@pytest.mark.parametrize("cmd_file,expected",
                         [('tests/testdata/test1.txt', '0,1,NORTH'),
                          ('tests/testdata/test2.txt', '0,0,WEST'),
                          ('tests/testdata/test3.txt', '3,3,NORTH')
                          ])
def test_main(cmd_file, expected):
    assert Process.start(cmd_file) == expected
