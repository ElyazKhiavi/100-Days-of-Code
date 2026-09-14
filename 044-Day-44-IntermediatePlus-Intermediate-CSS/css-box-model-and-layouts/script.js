/* ===== Copy-to-clipboard for code blocks ===== */
document.querySelectorAll('.copy-btn').forEach(btn => {
  btn.addEventListener('click', async () => {
    const code = btn.parentElement.querySelector('code');
    if (!code) return;

    try {
      await navigator.clipboard.writeText(code.innerText);
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

/* ===== Flexbox playground ===== */
const flexDemo = document.getElementById('flexDemo');

document.querySelectorAll('[data-flex-dir]').forEach(btn => {
  btn.addEventListener('click', () => {
    flexDemo.style.flexDirection = btn.dataset.flexDir;
    document.querySelectorAll('[data-flex-dir]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

document.querySelectorAll('[data-flex-justify]').forEach(btn => {
  btn.addEventListener('click', () => {
    flexDemo.style.justifyContent = btn.dataset.flexJustify;
    document.querySelectorAll('[data-flex-justify]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

document.querySelectorAll('[data-flex-align]').forEach(btn => {
  btn.addEventListener('click', () => {
    flexDemo.style.alignItems = btn.dataset.flexAlign;
    document.querySelectorAll('[data-flex-align]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

/* ===== Scroll-spy ===== */
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
    link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
  });
}

window.addEventListener('scroll', updateActiveNav, { passive: true });
window.addEventListener('load', updateActiveNav);