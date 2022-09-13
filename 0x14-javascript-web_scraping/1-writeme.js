#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');

const content = process.argv[3];
fs.writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
