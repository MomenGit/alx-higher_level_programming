#!/usr/bin/node
const stdout = require('process').stdout;
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          stdout.write(c);
        }
      }
    } else {
      this.print();
    }
  }
};
