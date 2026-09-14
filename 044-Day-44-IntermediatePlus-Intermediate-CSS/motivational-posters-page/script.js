/* =========================================================
   Motivational Posters — local data
   ========================================================= */

const posters = [
  {
    image:
      "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=80",
    title: "The climb is the reward.",
    quote:
      "Every step you take toward the summit is a victory in itself. The view from the top is earned, not given.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600&q=80",
    title: "Stars can't shine without darkness.",
    quote:
      "Your hardest moments are not the end of your story — they are the backdrop that makes your light visible.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1600&q=80",
    title: "Breathe. Begin again.",
    quote:
      "Every sunrise is a second chance. You do not have to carry yesterday into today.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&q=80",
    title: "Grow quietly. Shine loudly.",
    quote:
      "The tallest trees started as seeds nobody noticed. Your growth does not need an audience to be real.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=80",
    title: "Stillness is strength.",
    quote:
      "The ocean does not rush, yet it shapes coastlines. Patience is a power most people underestimate.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1600&q=80",
    title: "Adventure is out there.",
    quote:
      "You will never discover new oceans unless you have the courage to lose sight of the shore.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=1600&q=80",
    title: "Find peace in the journey.",
    quote:
      "The destination matters, but the road teaches you who you are. Do not sleepwalk through the miles.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=1600&q=80",
    title: "Water the roots first.",
    quote:
      "What you feed in the quiet will bloom in the open. Invest in the unseen parts of your life.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=1600&q=80",
    title: "Keep your face to the sun.",
    quote:
      "Shadows fall behind you when you turn toward the light. Perspective is a choice you make daily.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=1600&q=80",
    title: "One step at a time.",
    quote:
      "You do not need to see the whole staircase. Just take the next step — and the one after that.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=1600&q=80",
    title: "The best view comes after the hardest climb.",
    quote:
      "Nothing worth having is easy. The effort you put in today becomes the pride you feel tomorrow.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1444927714506-8492d94b4e3d?w=1600&q=80",
    title: "Your only limit is you.",
    quote:
      "Doubt kills more dreams than failure ever will. Bet on yourself — even when nobody else does.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=1600&q=80",
    title: "Nature does not hurry.",
    quote:
      "Yet everything is accomplished. Slow down. Trust the timing of your life.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=1600&q=80",
    title: "Let the light in.",
    quote:
      "You are allowed to feel joy even while you are still healing. Both can be true at once.",
  },
  {
    image:
      "https://images.unsplash.com/photo-1475924156734-496f6cac6ec1?w=1600&q=80",
    title: "Every storm runs out of rain.",
    quote:
      "This too shall pass. Hold on longer than the storm holds on to you.",
  },
];

/* ===== State ===== */
let currentIndex = 0;
let isDownloading = false;

/* ===== DOM refs ===== */
const stage = document.getElementById("posterStage");
const nextBtn = document.getElementById("nextBtn");
const downloadBtn = document.getElementById("downloadBtn");
const counter = document.getElementById("counter");
const toast = document.getElementById("toast");

/* ===== Utilities ===== */
function slugify(text) {
  return (
    text
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 60) || "poster"
  );
}

function showToast(message, isError = false) {
  toast.textContent = message;
  toast.classList.toggle("error", isError);
  toast.classList.add("show");
  clearTimeout(showToast._t);
  showToast._t = setTimeout(() => toast.classList.remove("show"), 2600);
}

/* Wraps a string into lines that fit within maxWidth, given ctx.font is set */
function wrapText(ctx, text, maxWidth) {
  const words = text.split(" ");
  const lines = [];
  let line = "";
  for (const word of words) {
    const test = line ? `${line} ${word}` : word;
    if (ctx.measureText(test).width > maxWidth && line) {
      lines.push(line);
      line = word;
    } else {
      line = test;
    }
  }
  if (line) lines.push(line);
  return lines;
}

/* ===== Render ===== */
function renderPoster(index) {
  const p = posters[index];

  stage.innerHTML = `
    <div class="poster-image">
      <img src="${p.image}" alt="${p.title}" crossorigin="anonymous" loading="lazy">
    </div>
    <div class="poster-content">
      <h2 class="poster-title">${p.title}</h2>
      <p class="poster-quote">${p.quote}</p>
    </div>
  `;

  // Re-trigger fade-in
  stage.style.animation = "none";
  void stage.offsetWidth;
  stage.style.animation = "";

  counter.textContent = `${index + 1} / ${posters.length}`;
}

/* ===== Next poster ===== */
function nextPoster() {
  currentIndex = (currentIndex + 1) % posters.length;
  renderPoster(currentIndex);
}

/* =========================================================
   Download the poster as a PNG
   Draws the image + gradient + title + quote onto a canvas
   and triggers a download named after the title.
   ========================================================= */
async function downloadPoster() {
  if (isDownloading) return;
  isDownloading = true;
  downloadBtn.disabled = true;
  const originalLabel = downloadBtn.innerHTML;
  downloadBtn.innerHTML = '<span class="btn-icon">⏳</span> Rendering…';
  showToast("Rendering poster…");

  try {
    const p = posters[currentIndex];

    // ---- Canvas setup (16:10 ratio, 1600 × 1000) ----
    const W = 1600;
    const H = 1000;
    const canvas = document.createElement("canvas");
    canvas.width = W;
    canvas.height = H;
    const ctx = canvas.getContext("2d");

    // ---- Load image with CORS ----
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.src = p.image;

    await new Promise((resolve, reject) => {
      img.onload = resolve;
      img.onerror = () => reject(new Error("Image failed to load"));
    });

    // ---- Draw image (object-fit: cover, centered) ----
    const imgRatio = img.width / img.height;
    const targetRatio = W / H;
    let dw, dh, dx, dy;

    if (imgRatio > targetRatio) {
      dh = H;
      dw = H * imgRatio;
      dx = (W - dw) / 2;
      dy = 0;
    } else {
      dw = W;
      dh = W / imgRatio;
      dx = 0;
      dy = (H - dh) / 2;
    }
    ctx.drawImage(img, dx, dy, dw, dh);

    // ---- Bottom gradient overlay (matches CSS) ----
    const gradient = ctx.createLinearGradient(0, H * 0.4, 0, H);
    gradient.addColorStop(0, "rgba(26, 15, 7, 0)");
    gradient.addColorStop(0.55, "rgba(26, 15, 7, 0.55)");
    gradient.addColorStop(1, "rgba(26, 15, 7, 0.95)");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, W, H);

    // ---- Text layout ----
    const padding = 80;
    const maxWidth = W - padding * 2;

    // Font setup — scaled up from the CSS version
    const titleFont = '700 72px Georgia, "Times New Roman", serif';
    const quoteFont =
      '400 30px system-ui, -apple-system, "Segoe UI", sans-serif';
    const titleLineHeight = 88;
    const quoteLineHeight = 44;

    // ---- Measure quote first (it sits at the very bottom) ----
    ctx.font = quoteFont;
    const quoteLines = wrapText(ctx, p.quote, maxWidth);

    // ---- Measure title ----
    ctx.font = titleFont;
    const titleLines = wrapText(ctx, p.title, maxWidth);

    // ---- Compute total block height and draw bottom-up ----
    const gap = 28;
    const quoteBlockHeight = quoteLines.length * quoteLineHeight;
    const titleBlockHeight = titleLines.length * titleLineHeight;
    const totalHeight = titleBlockHeight + gap + quoteBlockHeight;

    let y = H - padding - quoteBlockHeight; // top of the quote block

    // Draw title (above quote)
    ctx.font = titleFont;
    ctx.fillStyle = "#d4a373";
    ctx.textBaseline = "top";
    ctx.shadowColor = "rgba(0, 0, 0, 0.8)";
    ctx.shadowBlur = 16;
    ctx.shadowOffsetY = 3;

    let titleY = y - gap - titleBlockHeight;
    for (const line of titleLines) {
      ctx.fillText(line, padding, titleY);
      titleY += titleLineHeight;
    }

    // Draw quote
    ctx.font = quoteFont;
    ctx.fillStyle = "rgba(236, 224, 209, 0.94)";
    ctx.shadowBlur = 10;
    ctx.shadowOffsetY = 2;

    let quoteY = y;
    for (const line of quoteLines) {
      ctx.fillText(line, padding, quoteY);
      quoteY += quoteLineHeight;
    }

    // ---- Export ----
    const slug = slugify(p.title);

    const blob = await new Promise((resolve, reject) => {
      canvas.toBlob(
        (b) => (b ? resolve(b) : reject(new Error("toBlob failed"))),
        "image/png",
        0.95,
      );
    });

    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${slug}.png`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 4000);

    showToast(`Downloaded “${slug}.png”`);
  } catch (err) {
    console.error(err);
    showToast("Download failed — check your connection and try again.", true);
  } finally {
    isDownloading = false;
    downloadBtn.disabled = false;
    downloadBtn.innerHTML = originalLabel;
  }
}

/* ===== Events ===== */
nextBtn.addEventListener("click", nextPoster);
downloadBtn.addEventListener("click", downloadPoster);

document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
  if (e.key === "n" || e.key === "N" || e.key === " ") {
    e.preventDefault();
    nextPoster();
  }
  if (e.key === "d" || e.key === "D") {
    e.preventDefault();
    downloadPoster();
  }
});

/* ===== Init ===== */
renderPoster(currentIndex);
