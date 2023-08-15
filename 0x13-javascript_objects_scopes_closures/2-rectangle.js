#!/usr/bin/node

/*
Using the class notation for defining the class Rectangle.
*/

class Rectangle {
  constructor(width, height) {
    if (width <= 0 || height <= 0) {
      return {};
    }
    this.width = width;
    this.height = height;
  }
}
module.exports = Rectangle;
