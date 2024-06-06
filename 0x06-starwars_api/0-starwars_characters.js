#!/usr/bin/node

const axios = require('axios');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

async function fetchCharacterName(characterUrl) {
  try {
    const response = await axios.get(characterUrl);
    console.log(response.data.name);
  } catch (error) {
    console.error(`Error fetching character: ${error.message}`);
  }
}

async function fetchFilmCharacters() {
  try {
    const response = await axios.get(url);
    const characterUrls = response.data.characters;
    for (const characterUrl of characterUrls) {
      await fetchCharacterName(characterUrl);
    }
  } catch (error) {
    console.error(`Error fetching film: ${error.message}`);
  }
}

fetchFilmCharacters();

