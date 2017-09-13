# make-me-some-data
Make-me-some-data is a tool to procedurally generate some test data for search. It's pretty crap and we should probably replace it with something better, but it's not a bad tool for creating ALL THE DATA.

## Usage

### Generic
``` sh
$ node index.js <outputFile.json> [--amount <number>]
```

### Examples

Create a default amount of data (1,000 units)
``` sh
$ node index.js ./myData.json
```

Create a tiny dataset (5 units)
``` sh
$ node index.js ./myData.json --amount 5
```

Create a really big dataset (10,000 units)
``` sh
$ node index.js ./myData.json --amount 10000
```

Create data in search_bench
``` sh
$ node index.js ../../search_bench/resources/foo-data.json --amount 500
```