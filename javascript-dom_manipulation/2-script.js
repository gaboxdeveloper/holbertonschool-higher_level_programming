const red_header = document.getElementById('red_header');
const header = document.querySelector('header');
red_header.addEventListener('click', function() {
  header.classList.add('red');
});
