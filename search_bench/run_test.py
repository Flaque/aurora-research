import json
from subprocess import call


def run_tests(test_file):
"""
Runs a test file and all of its tests.

Params:
    test_file: should contain command, dataset_file, and tests.

Returns:
    ???
"""
    tests = load_json(test_file)

    dataset = test["dataset_file"]
    command = test["command"]
    metrics = []
    for test in tests["tests"]:
        metrics.append(test_search(dataset, command, test))

    # average/min/max metrics
    print metrics


def load_json(jfile):
"""
Loads json from a file
"""
    with open(jfile) as json_file:
        return json.load(json_file)


def test_search(dataset_file, command, test):
"""
Tests a specific search_text on the algorithm

Params:
    dataset_file: file containing our test dataset
    command: command to run search algorithm
    test: test object

Returns:
    Result hueristics
"""
    search_text = test["search_text"]
    n_results = len(test["results"])
    call([command, dataset_file, search_text, n_results])

    # read stdout of search algorithm
    #
    # run hueristics on results

    return None
