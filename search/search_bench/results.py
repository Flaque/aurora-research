
def parse_results(device_under_test_output):
    """
    The results function take the output of the device under test and return a map in the following format.

    PARAMS:
        device_under_test_output: string following the defined output of the search_bench protocol.abs

    OUTPUT:
    {
        setup_time(ms),
        search_time(ms),
        results:[
        "uuid",
        "uuid",
        "...",
        "uuid"
        ]
    }
    """

    output_lines = device_under_test_output.splitlines()
    parsed_results = {"query_results": []}
    state = None
    for output_line in output_lines:
        if not state:
            if output_line == "__RESULTS__":
                state = "setup_time"
                continue
            else:
                continue

        if output_line == "__END_RESULTS__":
            break

        if state == "setup_time":
            parsed_results["setup_time"] = int(output_line)
            state = "search_time"
        elif state == "search_time":
            parsed_results["search_time"] = int(output_line)
            state = "query_results"
        elif state == "query_results":
            parsed_results["query_results"].append(int(output_line))

    return parsed_results

def score(test_results_expected, device_under_test_results):
    """
    This function scores the results of the algorithm by comparing its output to the expected output.
    Scoring the algorithm by comparing the number of correct uuids produced as comparted to the expectation.

    PARAMS:
        test_results_expected:[strings] - this parameter should be a list of uuids that were expected.

        device_under_test_results:[strings] - this paramter should be a list of uuids that the device under
        test returned.

    OUTPUT
        float - the percentage of correct results that the algorithm returned indepdant of order.
    """

    test_set = set(test_results_expected)
    dut_set  = set(device_under_test_results)

    set_difference = test_set - dut_set
    return float(len(test_set) - len(set_difference)) / float(len(test_set))
