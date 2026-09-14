// ===== Card flipping =====
const cards = document.querySelectorAll('.card');
const counterEl = document.getElementById('counter');
const flipAllBtn = document.getElementById('flipAll');
const resetBtn = document.getElementById('resetAll');

function updateCounter() {
  const flipped = document.querySelectorAll('.card.flipped').length;
  counterEl.textContent = `${flipped} / ${cards.length} flipped`;

  // Update Flip All button label based on state
  const allFlipped = flipped === cards.length;
  flipAllBtn.textContent = allFlipped ? 'Flip Back' : 'Flip All';
}

// Individual card click
cards.forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('flipped');
    updateCounter();
  });
});

// Flip all / flip back
flipAllBtn.addEventListener('click', () => {
  const allFlipped = document.querySelectorAll('.card.flipped').length === cards.length;
  cards.forEach(card => {
    card.classList.toggle('flipped', !allFlipped);
  });
  updateCounter();
});

// Reset
resetBtn.addEventListener('click', () => {
  cards.forEach(card => card.classList.remove('flipped'));
  updateCounter();
});

// Keyboard shortcut: press "F" to flip all, "R" to reset
document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

  if (e.key === 'f' || e.key === 'F') {
    flipAllBtn.click();
  }
  if (e.key === 'r' || e.key === 'R') {
    resetBtn.click();
  }
});

// Init
updateCounter();