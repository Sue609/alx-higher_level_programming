#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments.
*/

const argv = require('process').argv;
const num = argv.length;

if (num <= 3) {
  console.log('0');
} else {
  let first = parseInt(argv[2]);
  let second = parseInt(argv[3]);

  if (second > first) {
    [first, second] = [second, first];
  }
  for (let i = 4; i < num; i++) {
    const nums = parseInt(argv[i]);
    if (nums > first) {
      second = first;
      first = nums;
    } else if (num > second && num < first) {
      second = num;
    }
  }
  console.log(second);
}
