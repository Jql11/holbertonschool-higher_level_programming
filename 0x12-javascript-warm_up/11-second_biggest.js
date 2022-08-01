#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length < 2) {
  console.log(0);
} else {
  console.log(arr.sort(function (a, b) { return b - a; })[1]);
}
