#!/usr/bin/node

const url = process.argv[2];
const axios = require('axios');

axios.get(url)
  .then(response => {
    console.log('code: ' + response.status);
  }).catch(error => {
    console.log(error);
  });
