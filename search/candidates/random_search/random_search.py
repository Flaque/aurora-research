import sys
import json
import datetime
import random

# etract command line args
data_file = sys.argv[1]
search_text = sys.argv[2]
n_result = int(sys.argv[3])

print("Reading in data")
data = None
with open(data_file) as json_file:
    data = json.load(json_file)

print("Searching")
# run our search algorithm: select random results!
a = datetime.datetime.now()
result_ids = []
for index in random.sample(range(0, len(data) - 1), n_result):
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
