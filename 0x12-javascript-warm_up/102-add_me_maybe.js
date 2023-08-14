#!/usr/bin/node
/*
Module that exports a function to increment and call another function.
*/

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
