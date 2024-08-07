#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];
request(API_URL + filmId, (err, _, body) => {
  if (err) {
    console.log(err);
  }
  const charactersURL = JSON.parse(body).characters;
  const charactersName = charactersURL.map(
    url => new Promise((resolve, reject) => {
      request(url, (promiseErr, __, charactersReqBody) => {
        if (promiseErr) {
          reject(promiseErr);
        }
        resolve(JSON.parse(charactersReqBody).name);
      });
    })
  );
  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(allErr => console.log(allErr));
});
