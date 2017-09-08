from results import parse_results, score
from run_test import run_test

print(parse_results("""

wejfoiwjoe fjiwe
weoifjwe oijfoiew
weojfoiwejfoiwej
weoifjwoiejfoiwe
woiejfoiwjeofijweoifjo

__RESULTS__
101
1000
ewoifjwioe
ofeijwoiejfiow
oiwejfoijweof
oiwfjeoifjwo
ofijweofjow
lwjefoiwej
__END_RESULTS__

foiwejfoiwejoif
fwjeiofjweiojf
"""))

print(score(["test", "woo"], ["test", "shoo"]))
