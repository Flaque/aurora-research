
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
            parsed_results["query_results"].append(output_line)

    
    return parsed_results
        


    

  
   
