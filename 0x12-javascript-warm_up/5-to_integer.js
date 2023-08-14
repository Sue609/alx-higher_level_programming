#!/usr/bin/node
/*
Script that converts number to an integer.
*/

const stringNum = process.argv[2];
const intValue = parseInt(stringNum);

if (!isNaN(intValue)) {
  console.log(`My number: ${intValue}`);
} else {
  console.log('Not a number');
}
