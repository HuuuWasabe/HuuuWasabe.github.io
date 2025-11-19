// js/dropdown.js
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.dropdown-toggle');
  const menu = document.querySelector('.dropdown-menu');
  const sidebarSection = document.getElementById('sidebar-section');

  toggle.addEventListener('click', (e) => {
    e.preventDefault();
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('show');
    sidebarSection.classList.toggle('active');
  });

  // Sidebar
  const sidebarItems = document.querySelectorAll('.sidebar-item');
  const contentBoxes = document.querySelectorAll('.sidebar-content-box');

  sidebarItems.forEach(item => {
    item.addEventListener('click', () =>{
       // Remove old active
       sidebarItems.forEach(i => i.classList.remove('active'));
       contentBoxes.forEach(b => b.classList.remove('active'));

       // Renew Active
       item.classList.add('active');
       const target = item.getAttribute('data-target');
       document.getElementById(target).classList.add('active');
       })
    })


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