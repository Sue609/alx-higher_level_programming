#!/usr/bin/node
/*
Script that prints two arguements passes to it.
*/

const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

console.log(arg1 + ' is ' + arg2);
