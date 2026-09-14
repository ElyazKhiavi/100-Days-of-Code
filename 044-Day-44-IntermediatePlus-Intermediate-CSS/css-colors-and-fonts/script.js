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

/* ===== Smooth scroll for anchor links ===== */
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

/* ===== Scroll-spy: highlight active nav link ===== */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.hero-nav a');

function updateActiveNav() {
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 120) {
      current = section.id;
    }
  });

  navLinks.forEach(link => {
    const isActive = link.getAttribute('href') === `#${current}`;
    link.style.background = isActive ? 'var(--brand)' : '';
    link.style.color      = isActive ? '#fff' : '';
    link.style.borderColor = isActive ? 'var(--coral)' : '';
  });
}

window.addEventListener('scroll', updateActiveNav, { passive: true });
window.addEventListener('load', updateActiveNav);