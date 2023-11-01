#!/usr/bin/node
// fetches and prints how to say “Hello” depending on the language

$(document).ready(() => {
  function translate () {
    const langCode = $('input#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, (data) => {
      $('div#hello').text(data.hello);
    });
  }
  $('input#btn_translate').click(translate);

  $('input#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});
