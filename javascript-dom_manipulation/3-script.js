// toggle header class between red and green when #toggle_header is clicked
const toggleHeader = document.querySelector('#toggle_header');
const header3 = document.querySelector('header');

if (toggleHeader && header3) {
  toggleHeader.addEventListener('click', () => {
    if (header3.classList.contains('red')) {
      header3.classList.remove('red');
      header3.classList.add('green');
    } else {
      header3.classList.remove('green');
      header3.classList.add('red');
    }
  });
}
