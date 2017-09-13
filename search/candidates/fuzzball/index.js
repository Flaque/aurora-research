const Fuse = require('fuse.js');
var fs = require("fs");

function get_args(args) {

}

function get_items_from_file(file) {
  var content = fs.readFileSync(file);
  return JSON.parse(content);
}

function populate_fuse(items) {

  var options = {
    threshold: 0.6,
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

var items = get_items_from_file("search_bench/resources/dataset1.json");
var fuse = populate_fuse(items);
var results = search_fuse(fuse, 'hello');

console.log(items);
console.log(results);
