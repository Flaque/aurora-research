# Search Bench
A "test-bench" like tool that facilitates standardized testing of various search algorithms on large datasets.

## Setup
Install tabulate
```
pip install tabulate
```

## Try it
From the root of this repo: (python3)
```
python search_bench/main.py canidates/random_search/test_batch1.json
```

or if you'd like pretty printed output, add a `-pretty` to the end of the command:
```
python search_bench/main.py canidates/random_search/test_batch1.json -pretty
```

## Use
To use this tool, you need three things:
1. A working search algorithm that can be called from the command line.
2. A `test-batch` file that defines how to use the tool and which test cases to run.
3. A `dataset` file that contains our "notes".

### 1. Search Algorithm
You can write your search algorithm in any language, but it must be run from the command line in this form:
```
some_commands ... DATASET_FILE SEARCH_TEXT NUMBER_OF_RESULTS
```
It should then run the search algorithm on the dataset and the desired search text and return the specified number of results. The output of the program should be:
```
...
__RESULTS__
<setup_time(ms)>
<search_time(ms)>
result1_uuid
result2_uuid
...
resultn_uuid
__END_RESULTS__
...
```

### 2. Test-batch file
This file will define how to run your algorithm and what specific search tests to run. It should be a json file of the format:
```
{
  "command":"run my_program",
  "dataset_file":"my_dataset.json",
  "tests": [
    {
      "search_text":"i want to search for this",
      "results": [5, 19, 33]
    }
    ...more tests
  ]
}
```
More details:
- the integers in `results` are the corresponding uuids of the results you expect your search algorithm to return from the data set.
- the `command` is the part of the command necessary to run your program that precedes the `dataset_file` arg. i.e. your program should be able to run like `command DATASET_FILE SEARCH_TEXT N_RESULTS`.
- the path to the `DATASET_FILE` should be from the root of the repo.

A good example of this file is  `random_search/test_batch1.json`.

### 3. Dataset file
The dataset file is a json file of the format:
```
[
  {
    "uuid":some_unique_integer,
    "text":"text_for_this_note",
    "tags":["tag1", "tag2"...]
  }
  ...more notes
]
```
There can be any number (0 included) of tags for each note.

A good example of this file is `search_bench/resources/dataset1.json`.

### Putting it all together
Once you have these three components, you can run your tests and search algorithms from the root of the repo:
```
python search_bench/main.py MY_TEST_BATCH_FILE
```

Enjoy! Happy Testing!
