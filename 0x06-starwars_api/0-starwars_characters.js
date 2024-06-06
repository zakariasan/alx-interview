#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Function to fetch and print character names
  function fetchCharacter(characterUrl, callback) {
    request(characterUrl, (err, response, body) => {
      if (err) {
        callback(err);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      callback(null);
    });
  }

  // Using a recursive function to ensure order
  function fetchCharactersInOrder(index) {
    if (index >= characterUrls.length) {
      return;
    }
    fetchCharacter(characterUrls[index], (err) => {
      if (err) {
        console.error(err);
        return;
      }
      fetchCharactersInOrder(index + 1);
    });
  }

  // Start fetching characters from index 0
  fetchCharactersInOrder(0);
});
