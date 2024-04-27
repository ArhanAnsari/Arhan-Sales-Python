document.querySelector('#submit-btn').addEventListener('click', (e) => {
  e.preventDefault();
  const name = document.querySelector('#name').value;
  const email = document.querySelector('#email').value;
  const phone = document.querySelector('#phone').value;
  const message = document.querySelector('#message').value;

  fetch('/process', {
    method: 'POST',
    body: JSON.stringify({name, email, phone, message}),
    headers: {'Content-Type': 'application/json'}
  })
  .then(() => {
    window.location.href = '/successful';
  })
  .catch((err) => console.error(err));
});
