#!/usr/bin/node
/*
Script that prints addition of two integers.
*/

function add (a, b) {
  return a + b;
}

const argv = require('process').argv;

if (argv.length !== 4) {
  console.log('NaN');
} else {
  const num1 = parseInt(argv[2]);
  const num2 = parseInt(argv[3]);

  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(add(num1, num2));
  } else {
    console.log('NaN');
  }
}
