#!/usr/bin/node
const id = process.argv[2];

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + id)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.log(error);
  });
