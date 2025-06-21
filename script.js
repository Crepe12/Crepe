let socket = io();
let currentRoom = "";
let currentPlayer = "X";

function joinRoom() {
  currentRoom = document.getElementById("room").value;
  socket.emit("join", { room: currentRoom });
}

socket.on("update_board", (board) => {
  let boardDiv = document.getElementById("board");
  boardDiv.innerHTML = "";
  board.forEach((cell, index) => {
    let div = document.createElement("div");
    div.className = "cell";
    div.textContent = cell;
    div.onclick = () => {
      socket.emit("move", {
        room: currentRoom,
        index: index,
        player: currentPlayer
      });
      currentPlayer = currentPlayer === "X" ? "O" : "X";
    };
    boardDiv.appendChild(div);
  });
});
