#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorialize (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(num));
