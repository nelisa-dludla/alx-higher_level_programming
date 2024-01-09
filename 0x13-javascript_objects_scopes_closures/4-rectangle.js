#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || !Number.isInteger(w) || h < 1 || !Number.isInteger(h)) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;

    while (i < this.height) {
      let j = 0;

      while (j < this.width) {
        process.stdout.write('X');
        j++;
      }
      console.log();
      i++;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
