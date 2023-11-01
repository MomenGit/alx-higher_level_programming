#!/usr/bin/node
/*
toggles the class of the <header> element
when the user clicks on the tag DIV#toggle_header
*/

$('div#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').attr('class', 'red');
  } else if ($('header').hasClass('red')) {
    $('header').attr('class', 'green');
  }
});
