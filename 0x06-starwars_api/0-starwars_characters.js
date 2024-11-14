#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie:
 * - The first positional argument passed is the Movie ID
 *    - example: 3 = “Return of the Jedi”
 * - Displays one character name per line in the same order as the `characters` list in the /films/ endpoint
 * - Uses the `request` module
 */
const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

request.get(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (!err) {
      // get actors and follow their urls
      const actors = JSON.parse(body)?.characters;
      const characters = actors.map((actorUrl) => {
        return new Promise((resolve, reject) => {
          request.get(actorUrl, (err, res, body) => {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(body));
            }
          });
        });
      });

      Promise.all(characters).then((chars) => {
        chars.forEach((char) => {
          console.log(char.name);
        });
      });
    }
  }
);
