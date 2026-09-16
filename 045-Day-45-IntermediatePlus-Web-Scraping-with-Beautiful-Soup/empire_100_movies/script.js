/* =========================================================
   Movie Gallery
   ---------------------------------------------------------
   Fetches data.json (served via `python -m http.server`),
   renders one card per movie, and lets you click any card
   to toggle it as watched.

   No persistence — state resets on refresh, by design.
   ========================================================= */

const grid = document.getElementById("movieGrid");
const counterEl = document.getElementById("watchedCounter");
const loadingMsg = document.getElementById("loadingMsg");

let totalMovies = 0;
let watchedCount = 0;

/* ===== Update the header counter ===== */
function updateCounter() {
  counterEl.textContent = `${watchedCount} watched · ${totalMovies - watchedCount} remaining`;
}

/* ===== Toggle a card's watched state ===== */
function toggleWatched(card) {
  const isNowWatched = card.classList.toggle("watched");
  watchedCount += isNowWatched ? 1 : -1;
  updateCounter();
}

/* ===== Build a single card ===== */
function createCard(movie) {
  const card = document.createElement("article");
  card.className = "movie-card";
  card.dataset.rank = movie.rank ?? "";

  card.innerHTML = `
    <div class="still">
      <img
        src="${movie.img_url || ""}"
        alt="${movie.title || "Movie"} still"
        class="still-img"
        loading="lazy">
      <span class="rank">#${movie.rank ?? "—"}</span>
    </div>
    <div class="movie-body">
      <header class="movie-header">
        <h2 class="movie-title">${movie.title || "Untitled"}</h2>
        <span class="year">${movie.year ?? "—"}</span>
      </header>
      <dl class="movie-credits">
        <dt>Director</dt>
        <dd>${movie.director || "—"}</dd>
        <dt>Starring</dt>
        <dd>${movie.starring || "—"}</dd>
      </dl>
    </div>
  `;

  card.addEventListener("click", () => toggleWatched(card));
  return card;
}

/* ===== Load and render ===== */
async function loadMovies() {
  try {
    const res = await fetch("data.json", { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const payload = await res.json();
    const movies = payload.data || [];

    if (!movies.length) {
      loadingMsg.textContent = "No movies found in data.json.";
      return;
    }

    grid.innerHTML = "";
    totalMovies = movies.length;

    const frag = document.createDocumentFragment();
    movies.forEach((movie) => frag.appendChild(createCard(movie)));
    grid.appendChild(frag);

    updateCounter();
    console.log(`[movie-gallery] rendered ${totalMovies} movie(s).`);
  } catch (err) {
    console.error("[movie-gallery] failed to load data.json:", err);
    loadingMsg.innerHTML = `
      Could not load <code>data.json</code>.<br>
      <span style="font-size:0.8rem;opacity:0.7">
        Serve the folder with <code>python -m http.server 8000</code>
        and open <code>http://localhost:8000</code>.
      </span>
    `;
    loadingMsg.classList.add("error");
  }
}

/* ===== Go ===== */
loadMovies();
