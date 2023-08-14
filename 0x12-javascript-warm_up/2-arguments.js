#!/usr/bin/node
/*
Script that prints a message depending of the number of arguements.
*/

if (process.argv.length === 2) {
  console.log('No Arguement');
} else if (process.argv.length === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
