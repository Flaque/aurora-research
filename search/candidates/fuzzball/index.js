const Fuse = require('fuse.js');

function get_args(argv) {
argsObj={
  "dataset_file":argv[2],
  "search_text":argv[3],
  "n_results":Number(argv[4])
  }
  return argsObj;
}

function populate_fuse(items) {

}

function search_fuse(fuse) {

}

console.log('Hello world');
console.log(get_args(process.argv));
