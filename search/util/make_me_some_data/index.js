const argv = require("minimist")(process.argv.slice(2));
const fs = require("fs");
const path = require("path");
const data = require("./data.js");

// Grab the main output argument
const outputFile = argv._[0];
const outputFilePath = path.resolve(outputFile);

// Get an amount if there is one, otherwise just make 1000
let amount = argv.amount ? argv.amount : 1000;
if (amount > 50) console.log("Creating data. this might take a moment...");

fs.writeFileSync(outputFilePath, JSON.stringify(data(amount)));

console.log(`Hurray! We wrote ${amount} pieces of data to "${outputFilePath}"`);
