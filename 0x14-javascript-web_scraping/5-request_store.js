#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];
const filepath = process.argv[3];
const fs = require('fs');

axios
  .get(url)
  .then(response => {
    const content = response.data;
    fs.writeFile(filepath, content, err => {
      if (err) {
        console.log(err);
      }
    });
  });
