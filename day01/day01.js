
// read input.txt line by line
const fs = require('fs');

// Read the file input.txt
const data = fs.readFileSync('input.txt', 'utf-8');
// Split the file content by new lines into an array
const lines = data.split('\n');
console.log("read " + lines.length + " lines");

// implement your code here
// ...



// print the result in here 