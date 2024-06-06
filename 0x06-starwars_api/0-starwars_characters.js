#!/usr/bin/node

const request = require("request");
const name = process.argv[2];
const link = `https://swapi-api.hbtn.io/api/films/${name}`;

request(link, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  for (const charId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(charId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
