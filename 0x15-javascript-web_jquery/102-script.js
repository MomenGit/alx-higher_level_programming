#!/usr/bin/node
// fetches and prints how to say “Hello” depending on the language

$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const langCode = $('input#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, (data) => {
      $('div#hello').text(data.hello);
    });
  });
});
