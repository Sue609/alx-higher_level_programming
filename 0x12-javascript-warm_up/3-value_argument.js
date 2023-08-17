#!/usr/bin/node
/*
Script that prints the first arguement passed.
*/

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
