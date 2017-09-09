from results import parse_results
from run_test import run_tests
import sys

# print(parse_results("""
#
# wejfoiwjoe fjiwe
# weoifjwe oijfoiew
# weojfoiwejfoiwej
# weoifjwoiejfoiwe
# woiejfoiwjeofijweoifjo
#
# __RESULTS__
# 101
# 1000
# ewoifjwioe
# ofeijwoiejfiow
# oiwejfoijweof
# oiwfjeoifjwo
# ofijweofjow
# lwjefoiwej
# __END_RESULTS__
#
# foiwejfoiwejoif
# fwjeiofjweiojf
# """))


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
