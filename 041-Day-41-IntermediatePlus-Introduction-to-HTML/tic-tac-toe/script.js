// ===== State =====
const WINNING_COMBOS = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8], // rows
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8], // cols
  [0, 4, 8],
  [2, 4, 6], // diagonals
];

let board = Array(9).fill("");
let currentPlayer = "X";
let gameOver = false;
let scores = { X: 0, O: 0, draw: 0 };

// ===== DOM =====
const cells = document.querySelectorAll(".cell");
const statusEl = document.getElementById("status");
const resetBtn = document.getElementById("resetBtn");
const scoreXEl = document.getElementById("scoreX");
const scoreOEl = document.getElementById("scoreO");
const scoreDrawEl = document.getElementById("scoreDraw");

// ===== Core logic =====
function handleClick(e) {
  const cell = e.currentTarget;
  const index = +cell.dataset.index;

  if (gameOver || board[index]) return;

  board[index] = currentPlayer;
  cell.textContent = currentPlayer;
  cell.classList.add(currentPlayer.toLowerCase());
  cell.disabled = true;

  const result = checkResult();

  if (result) {
    endGame(result);
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  updateStatus();
}

function checkResult() {
  // Check for a winner
  for (const combo of WINNING_COMBOS) {
    const [a, b, c] = combo;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return { winner: board[a], combo };
    }
  }
  // Check for a draw
  if (board.every((cell) => cell)) {
    return { winner: "draw", combo: null };
  }
  return null;
}

function endGame(result) {
  gameOver = true;

  if (result.winner === "draw") {
    scores.draw++;
    statusEl.innerHTML = `It's a <span class="text-[#99aab5]">draw</span>!`;
  } else {
    scores[result.winner]++;
    result.combo.forEach((i) => cells[i].classList.add("win"));
    statusEl.innerHTML = `Player <span class="text-[#7289da]">${result.winner}</span> wins!`;
  }

  updateScores();
  cells.forEach((cell) => (cell.disabled = true));
}

function updateStatus() {
  const color = currentPlayer === "X" ? "#7289da" : "#ffffff";
  statusEl.innerHTML = `Player <span style="color:${color}">${currentPlayer}</span>'s turn`;
}

function updateScores() {
  scoreXEl.textContent = scores.X;
  scoreOEl.textContent = scores.O;
  scoreDrawEl.textContent = scores.draw;
}

function resetBoard() {
  board = Array(9).fill("");
  currentPlayer = "X";
  gameOver = false;

  cells.forEach((cell) => {
    cell.textContent = "";
    cell.disabled = false;
    cell.classList.remove("x", "o", "win");
  });

  updateStatus();
}

// ===== Events =====
cells.forEach((cell) => cell.addEventListener("click", handleClick));
resetBtn.addEventListener("click", resetBoard);

// ===== Init =====
updateStatus();
updateScores();
