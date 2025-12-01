// list all star wars film titles inside the #list_movies element
document.addEventListener('DOMContentLoaded', () => {
  const list = document.querySelector('#list_movies');

  if (!list) {
    return;
  }

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => response.json())
    .then((data) => {
      if (!data.results) {
        return;
      }
      data.results.forEach((film) => {
        const li = document.createElement('li');
        li.textContent = film.title;
        list.appendChild(li);
      });
    })
    .catch(() => {
      // if the request fails, just leave the list empty
    });
});
