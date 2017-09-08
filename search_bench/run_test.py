import json
from subprocess import call


def run_tests(test_file):
    tests = load_json(test_file)

    dataset = test["dataset_file"]
    command = test["command"]
    metrics = []
    for test in tests["tests"]:
        metrics.append(test_search(dataset, command, test))

    # average/min/max metrics
    print metrics


def load_json(jfile):
    with open(jfile) as json_file:
        return json.load(json_file)


def test_search(dataset_file, command, test):
    search_text = test["search_text"]
    n_results = len(test["results"])
    call([command, dataset_file, search_text, n_results])

    # read stdout of search algorithm
    #
    # run hueristics on results

    return None
