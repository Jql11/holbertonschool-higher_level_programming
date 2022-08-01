#!/usr/bin/node
function nextBiggest (arr) {
  let max = -Infinity; let result = -Infinity;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr]; // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }

  return result;
}

if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(nextBiggest(process.argv));
}
