#!/usr/bin/node
const { stdout } = require('process');
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          stdout.write(c);
        }
        stdout.write('\n');
      }
    } else {
      this.print();
    }
  }
};
