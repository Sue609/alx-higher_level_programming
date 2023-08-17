#!/usr/bin/node

let arguements = 0;

exports.logMe = function (item) {
  console.log(arguements + ': ' + item);
  arguements++;
};
