#!/usr/bin/node
const arg = process.argv;
if (arg.length <= 3) {
  console.log(0);
} else {
  arg.sort(function (a, b) { return b - a; });
  console.log(arg[3]);
}
