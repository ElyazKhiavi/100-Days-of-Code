// ===== Mobile menu toggle =====
const menuBtn = document.getElementById("menuBtn");
const mobileNav = document.getElementById("mobileNav");

menuBtn.addEventListener("click", () => {
  mobileNav.classList.toggle("hidden");
});

// Close mobile menu when a link is clicked
mobileNav.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    mobileNav.classList.add("hidden");
  });
});

// ===== Smooth scroll for all anchor links =====
document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (e) => {
    const targetId = link.getAttribute("href");
    if (targetId === "#") return;
    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// ===== Active nav highlight on scroll =====
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll('header nav a[href^="#"]');

window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    const isActive = link.getAttribute("href") === `#${current}`;
    link.classList.toggle("text-white", isActive);
    link.classList.toggle("text-[#b3cde0]", !isActive);
  });
});

// ===== Animated stat counters =====
const counters = document.querySelectorAll("[data-count]");
let counted = false;

function animateCounters() {
  if (counted) return;
  const statsSection = document.getElementById("stats");
  const rect = statsSection.getBoundingClientRect();

  if (rect.top < window.innerHeight - 100) {
    counted = true;

    counters.forEach((counter) => {
      const target = +counter.getAttribute("data-count");
      const duration = 1200;
      const step = target / (duration / 16);
      let current = 0;

      const update = () => {
        current += step;
        if (current < target) {
          counter.textContent = Math.floor(current);
          requestAnimationFrame(update);
        } else {
          counter.textContent = target;
        }
      };
      update();
    });
  }
}

window.addEventListener("scroll", animateCounters);
window.addEventListener("load", animateCounters);

// ===== Contact form handling =====
const form = document.getElementById("contactForm");
const status = document.getElementById("formStatus");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = form.name.value.trim();
  const email = form.email.value.trim();
  const message = form.message.value.trim();

  if (!name || !email || !message) {
    status.textContent = "Please fill in all fields.";
    status.classList.remove("text-[#005b96]");
    status.classList.add("text-red-500");
    return;
  }

  status.textContent = `Thanks, ${name}! Your message has been sent.`;
  status.classList.remove("text-red-500");
  status.classList.add("text-[#005b96]");

  form.reset();

  setTimeout(() => {
    status.textContent = "";
  }, 5000);
});
