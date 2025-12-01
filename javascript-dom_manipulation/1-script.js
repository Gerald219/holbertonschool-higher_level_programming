// when clicking on the #red_header div, make the header text red
const redHeader = document.querySelector('#red_header');
const header1 = document.querySelector('header');

if (redHeader && header1) {
  redHeader.addEventListener('click', () => {
    header1.style.color = '#FF0000';
  });
}
