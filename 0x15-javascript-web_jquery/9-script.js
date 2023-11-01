#!/usr/bin/node
/*
fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and
displays the value of hello from that fetch in the HTML tag DIV#hello
*/

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  $('div#hello').text(data.hello);
});
