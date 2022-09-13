#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(response => {
    const tasks = response.data;
    const dict = {};
    for (const i in tasks) {
      const completion = tasks[i].completed;
      if (completion === true) {
        if (dict[tasks[i].userId] === undefined) {
          dict[tasks[i].userId] = 1;
        } else {
          dict[tasks[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  })
  .catch(error => {
    console.error(error);
  });
