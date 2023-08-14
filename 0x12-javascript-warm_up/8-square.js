#!/usr/bin/node
/*
script that prints a square.
*/

const stringNum = process.argv[2];
const intValue = parseInt(stringNum);

if (!isNaN(intValue)) {
  for (let i = 0; i < intValue; i++) {
    let row = '';
    for (let j = 0; j < intValue; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
