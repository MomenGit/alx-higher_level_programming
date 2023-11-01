#!/usr/bin/node
// comment

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  console.log(data);
  $('div#character').text(data.name);
});
