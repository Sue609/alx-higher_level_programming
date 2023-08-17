#!/usr/bin/node
/*
Module that exports a function to execute another function x times.
*/

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
