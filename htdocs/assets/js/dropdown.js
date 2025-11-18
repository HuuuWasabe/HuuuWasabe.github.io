// js/dropdown.js
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.dropdown-toggle');
  const menu = document.querySelector('.dropdown-menu');

  toggle.addEventListener('click', (e) => {
    e.preventDefault();
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('show');
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!toggle.contains(e.target) && !menu.contains(e.target)) {
      menu.classList.remove('show');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Close with Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      menu.classList.remove('show');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
});