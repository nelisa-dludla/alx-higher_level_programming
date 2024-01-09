#!/usr/bin/node

const parentSquare = require('./5-square.js');

class Square extends parentSquare {
  constructor (size) {
    super(size);
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
