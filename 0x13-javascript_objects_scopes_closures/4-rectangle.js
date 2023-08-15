#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = h;
      this.height = w;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    let newWidth = this.height;
    this.height = this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
