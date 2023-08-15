#!/usr/bin/node
/*
Create an instance method called print() that prints the rectangle using the character X
*/

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'x';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
