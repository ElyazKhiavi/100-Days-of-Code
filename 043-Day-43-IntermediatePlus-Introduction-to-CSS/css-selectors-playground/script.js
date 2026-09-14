/* ===== Copy-to-clipboard for code blocks ===== */
document.querySelectorAll('.copy-btn').forEach(btn => {
  btn.addEventListener('click', async () => {
    const code = btn.parentElement.querySelector('code');
    if (!code) return;

    const text = code.innerText;

    try {
      await navigator.clipboard.writeText(text);
      btn.textContent = 'Copied!';
      btn.classList.add('copied');

      setTimeout(() => {
        btn.textContent = 'Copy';
        btn.classList.remove('copied');
      }, 1400);
    } catch {
      btn.textContent = 'Failed';
      setTimeout(() => { btn.textContent = 'Copy'; }, 1400);
    }
  });
});

/* ===== Smooth scroll for in-page anchors ===== */
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const id = link.getAttribute('href');
    if (id === '#') return;

    const target = document.querySelector(id);
    if (!target) return;

    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

/* ===== Active nav highlight (scroll spy) ===== */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.hero-nav a');

function updateActiveNav() {
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 150) {
      current = section.id;
    }
  });

  navLinks.forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
  });
}

window.addEventListener('scroll', updateActiveNav, { passive: true });
window.addEventListener('load', updateActiveNav);