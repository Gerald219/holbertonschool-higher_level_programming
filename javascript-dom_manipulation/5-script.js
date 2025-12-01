// change the header text to 'New Header!!!' when #update_header is clicked
const updateHeader = document.querySelector('#update_header');
const header5 = document.querySelector('header');

if (updateHeader && header5) {
  updateHeader.addEventListener('click', () => {
    header5.textContent = 'New Header!!!';
  });
}
