// when clicking on the #red_header div, add the red class to the header
const redHeader2 = document.querySelector('#red_header');
const header2 = document.querySelector('header');

if (redHeader2 && header2) {
  redHeader2.addEventListener('click', () => {
    header2.classList.add('red');
  });
}
