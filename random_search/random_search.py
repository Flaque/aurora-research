import sys
import json
import datetime
from random import randint

# etract command line args
data_file = sys.argv[1]
search_text = sys.argv[2]
n_result = int(sys.argv[3])

# load in data
data = None
with open(data_file) as json_file:
    data = json.load(json_file)

# run our search algorithm: select random results!
a = datetime.datetime.now()
result_ids = []
for _ in range(n_result):
    index = randint(0, len(data)-1)
    result_id = data[index]["uuid"]
    result_ids.append(result_id)
elapsed = datetime.datetime.now() - a
ms = elapsed.microseconds / 100

print("__RESULTS__")
print("0")
print(ms)
for rid in result_ids:
    print(rid)
print("__END_RESULTS__")
