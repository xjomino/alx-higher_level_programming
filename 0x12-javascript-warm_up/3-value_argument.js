#!/usr/bin/node

const [_, __, arg1] = process.argv;

if (arg1 === undefined) {
  console.log("No argument");
} else {
  console.log(arg1);
}
