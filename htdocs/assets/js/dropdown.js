document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.dropdown-toggle');
  const menu    = document.querySelector('.dropdown-menu');

  // 1. Click the trigger
  toggle.addEventListener('click', e => {
    e.preventDefault();                 // don’t follow #
    menu.classList.toggle('show');
  });

  // 2. Click anywhere else → close
  document.addEventListener('click', e => {
    if (!toggle.contains(e.target) && !menu.contains(e.target)) {
      menu.classList.remove('show');
    }
  });

  // 3. Optional: close with ESC key
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') menu.classList.remove('show');
  });
});