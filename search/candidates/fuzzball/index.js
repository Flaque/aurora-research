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
    shouldSort: true, // puts best match first
    threshold: 0.9, // 0 requires perfect match, 1 will match everything
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 1,
    keys: [
      "text"  // TODO: search by tags also
    ]
  };

  return new Fuse(items, options);
}

function search_fuse(fuse, search_text, n_results) {
  return fuse.search(search_text).slice(0, n_results);
}

function get_result_ids(results) {
  return results.map(function(note) {return note.uuid;});
}

// ---------------- Main ------------------

var args = get_args(process.argv);
var items = get_items_from_file(args['dataset_file']);

var start_setup= new Date();
var fuse = populate_fuse(items);
var end_setup= new Date();

var setup_time= new Date();
setup_time.setTime(end_setup.getTime() - start_setup.getTime());
var setup_time_ms= setup_time.getMilliseconds();

var search_start= new Date();
var results = search_fuse(fuse, args['search_text'], args['n_results']);
var search_end = new Date();

var search_time = new Date();
search_time.setTime(search_end.getTime() - search_start.getTime());
var search_time_ms=search_time.getMilliseconds();

var result_ids = get_result_ids(results);
// print out results in proper format
console.log("__RESULTS__");
console.log(setup_time_ms);
console.log(search_time_ms);
result_ids.forEach(function(id) {
    console.log(id);
});
console.log("__END_RESULTS__");
