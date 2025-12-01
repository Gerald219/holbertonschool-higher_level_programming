// translate hello based on the selected language code and show it in #hello
document.addEventListener('DOMContentLoaded', () => {
  const select = document.querySelector('#language_code');
  const button = document.querySelector('#btn_translate');
  const helloDiv = document.querySelector('#hello');

  if (!select || !button || !helloDiv) {
    return;
  }

  const translate = () => {
    const lang = select.value;

    if (!lang) {
      helloDiv.textContent = '';
      return;
    }

    const url = `https://hellosalut.stefanbohacek.com/?lang=${lang}`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        helloDiv.textContent = data.hello;
      })
      .catch(() => {
        helloDiv.textContent = '';
      });
  };

  button.addEventListener('click', translate);
});
