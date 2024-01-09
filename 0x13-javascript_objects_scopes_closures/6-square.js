#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    const char = (c) || 'X';

    while (i < this.height) {
      let j = 0;

      while (j < this.width) {
        process.stdout.write(char);
        j++;
      }
      console.log();
      i++;
    }
  }
}

module.exports = Square;
