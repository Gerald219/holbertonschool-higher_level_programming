// show the french hello translation inside the #hello element
document.addEventListener('DOMContentLoaded', () => {
  const helloDiv = document.querySelector('#hello');

  if (!helloDiv) {
    return;
  }

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      helloDiv.textContent = data.hello;
    })
    .catch(() => {
      helloDiv.textContent = '';
    });
});
