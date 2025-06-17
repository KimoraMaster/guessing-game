function choose(direction) {
  const story = document.getElementById("story");

  if (direction === "left") {
    story.textContent = "You find a hidden treasure chest! You win!";
  } else if (direction === "right") {
    story.textContent = "You fall into a trap! Game over!";
  }
}
