#!/usr/bin/node
// Updates the text color of the <header> element to red (#FF0000)

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');

  header.style.color = '#FF0000';
});
