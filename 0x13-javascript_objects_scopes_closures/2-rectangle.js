#!/usr/bin/node

/*
Using the class notation for defining the class Rectangle.
*/

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
