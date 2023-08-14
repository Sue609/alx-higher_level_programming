#!/usr/bin/node
/*
script that prints x times.
*/

const argv = require('process').argv;

if (argv.length !== 3) {
  console.log('Missing number of occurences');
} else {
  const numTimes = parseInt(argv[2]);
  if (!isNaN(numTimes)) {
    for (let i = 0; i < numTimes; i++) {
      console.log('C is fun');
    }
  }
}
