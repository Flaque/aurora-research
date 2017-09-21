from results import parse_results
from run_test import run_tests
import sys


def hasPrettyFlag():
    if len(sys.argv) < 3:
        return False
    if sys.argv[2] == "-pretty":
        return True
    raise Exception(
        "Bad Input", "Expecting pretty flag, but got something else.")


test_file = sys.argv[1]
isPretty = True if hasPrettyFlag() else False
run_tests(test_file, isPretty)
