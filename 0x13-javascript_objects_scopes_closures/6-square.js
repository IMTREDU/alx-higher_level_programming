#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      let line = '';
      for (let col = 0; col < this.width; col++) {
        line += char;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
