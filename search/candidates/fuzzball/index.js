const Fuse = require('fuse.js');
var fs = require("fs");

function get_args(argv) {
  argsObj={
    "dataset_file":argv[2],
    "search_text":argv[3],
    "n_results":Number(argv[4])
  }
  return argsObj;
}

function get_items_from_file(file) {
  var content = fs.readFileSync(file);
  return JSON.parse(content);
}

function populate_fuse(items) {

  var options = {
    shouldSort: true,
    threshold: 0.9,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 1,
    keys: [
      "text"
    ]
  };

  return new Fuse(items, options);
}

function search_fuse(fuse, search_text) {
  return fuse.search(search_text);
}

var args = get_args(process.argv);
var items = get_items_from_file(args['dataset_file']);
var fuse = populate_fuse(items);
var results = search_fuse(fuse, args['search_text']);

console.log(results);
