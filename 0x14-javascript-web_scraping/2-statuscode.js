#!/usr/bin/node
const https = require('https');
const url = process.argv[2];

https.get(url, function (res) {
  console.log('code: ', res.statusCode);
});
