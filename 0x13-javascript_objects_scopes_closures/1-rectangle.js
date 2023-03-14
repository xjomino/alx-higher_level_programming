#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }

  area() {
    return this.width * this.height;
  }
}
