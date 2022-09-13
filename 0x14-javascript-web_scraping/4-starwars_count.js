#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(response => {
    const films = response.data.results;
    let count = 0;
    for (const features of films) {
      for (const people of features.characters) {
        if (people.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.error(error);
  });
