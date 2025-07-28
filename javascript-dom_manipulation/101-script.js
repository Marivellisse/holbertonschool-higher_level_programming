document.addEventListener('DOMContentLoaded', function () {
  const button = document.getElementById('btn_translate');
  const languageSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  button.addEventListener('click', function () {
    const langCode = languageSelect.value;

    if (langCode) {
      const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

      fetch(url)
        .then(response => response.json())
        .then(data => {
          helloDiv.textContent = data.hello;
        })
        .catch(error => {
          console.error('Error fetching translation:', error);
          helloDiv.textContent = 'Translation unavailable';
        });
    } else {
      helloDiv.textContent = 'Please select a language code';
    }
  });
});

