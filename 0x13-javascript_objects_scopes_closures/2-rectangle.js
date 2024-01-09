#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || !Number.isInteger(w) || h < 1 || !Number.isInteger(h)) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
