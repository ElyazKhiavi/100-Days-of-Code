/* =========================================================
   Movie Gallery — placeholder for Python-generated data
   ---------------------------------------------------------
   For now, this file only:
     • logs how many cards exist
     • marks the first card as active
     • exposes a helper so a future Python pass can
       add movies without touching the HTML by hand
   ========================================================= */

/* ===== Current cards ===== */
const cards = document.querySelectorAll('.movie-card');
console.log(`[movie-gallery] ${cards.length} card(s) on the page.`);

/* ===== Highlight on click (nice-to-have) ===== */
cards.forEach(card => {
  card.addEventListener('click', () => {
    cards.forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    console.log('[movie-gallery] selected:', card.dataset.movieId);
  });
});

/* =========================================================
   addMovie(movie) — helper for Python-driven rendering
   ---------------------------------------------------------
   Call this from a future script tag or from an injected
   JS block to append a movie card without duplicating HTML.

   Example (what Python might eventually output):

     addMovie({
       id:       "tt0114814",
       title:    "The Usual Suspects",
       year:     1995,
       genre:    "Crime",
       rating:   8.5,
       poster:   "https://image.tmdb.org/t/p/w500/...",
       desc:     "A sole survivor tells of the twisty events..."
     });
   ========================================================= */
window.addMovie = function addMovie(movie) {
  const grid = document.getElementById('movieGrid');
  if (!grid) return;

  const card = document.createElement('article');
  card.className = 'movie-card';
  card.dataset.movieId = movie.id || '';

  card.innerHTML = `
    <div class="poster">
      <img
        src="${movie.poster || 'https://via.placeholder.com/500x750/3d2657/cca3ff?text=Poster'}"
        alt="${(movie.title || 'Movie') + ' poster'}"
        class="poster-img"
        loading="lazy">
      <span class="rating" data-rating="${movie.rating ?? ''}">
        ${movie.rating != null ? Number(movie.rating).toFixed(1) : '—'}
      </span>
    </div>
    <div class="movie-body">
      <h2 class="movie-title">${movie.title || 'Untitled'}</h2>
      <p class="movie-meta">
        <span class="year">${movie.year || '—'}</span>
        <span class="dot">·</span>
        <span class="genre">${movie.genre || '—'}</span>
      </p>
      <p class="movie-desc">${movie.desc || ''}</p>
    </div>
  `;

  grid.appendChild(card);

  // Re-bind click handler for the new card
  card.addEventListener('click', () => {
    document.querySelectorAll('.movie-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    console.log('[movie-gallery] selected:', card.dataset.movieId);
  });
};