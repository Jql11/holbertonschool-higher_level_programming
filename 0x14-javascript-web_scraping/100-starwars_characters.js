#!/usr/bin/node
const id = process.argv[2];

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + id)
  .then(response => {
    const chars = response.data.characters;
    for (const name in chars) {
      axios.get(chars[name])
        .then(resp => {
          console.log(resp.data.name);
        });
    }
  })
  .catch(error => {
    console.log(error);
  });
