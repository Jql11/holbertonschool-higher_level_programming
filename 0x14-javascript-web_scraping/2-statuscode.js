#!/usr/bin/node

let url = process.argv[2];
const request = require('request');

request(url, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
