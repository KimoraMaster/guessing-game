const storyText = document.getElementById("story");
const choicesDiv = document.getElementById("choices");

const story = {
  start: {
    text: "You wake up in a dusty bedroom. The house groans with age. There's a door slightly open.",
    choices: [
      { text: "Leave the room", next: "hallway" },
      { text: "Look under the bed", next: "underBed" }
    ]
  },
  hallway: {
    text: "The hallway is dark. The wallpaper peels like dead skin. At the end is a door glowing faintly.",
    choices: [
      { text: "Go to the glowing door", next: "portalRoom" },
      { text: "Explore the bathroom", next: "bathroom" }
    ]
  },
  underBed: {
    text: "You find a strange old key covered in dust. It might be important.",
    choices: [
      { text: "Take the key and leave the room", next: "hallway" }
    ]
  },
  bathroom: {
    text: "The mirror is cracked. You see yourself... and something behind you. You turn, but nothing's there.",
    choices: [
      { text: "Run to the glowing door", next: "portalRoom" }
    ]
  },
  portalRoom: {
    text: "You enter a room filled with swirling fog. A mirror shows a strange, vibrant world. You step through...",
    choices: [
      { text: "Enter the strange world", next: "wonderlandEntrance" }
    ]
  },
  wonderlandEntrance: {
    text: "You're in a twisted forest. The trees whisper. A creature with a stitched smile approaches.",
    choices: [
      { text: "Talk to the creature", next: "creatureTalk" },
      { text: "Hide behind a tree", next: "hideTree" }
    ]
  },
  creatureTalk: {
    text: `"Welcome, stranger," it grins. "This world eats fear. What are you afraid of?"`,
    choices: [
      { text: `"I'm not afraid of anything."`, next: "braveryPath" },
      { text: `"Losing my mind."`, next: "fearPath" }
    ]
  },
  hideTree: {
    text: "The creature sniffs the air and vanishes. But now the trees are staring at you. The forest is awake.",
    choices: [
      { text: "Run deeper into the forest", next: "forestRun" },
      { text: "Climb a tree", next: "treeClimb" }
    ]
  },
  // More nodes like braveryPath, fearPath, forestRun, treeClimb, etc. can be added!
};

function showNode(nodeKey) {
  const node = story[nodeKey];
  storyText.textContent = node.text;
  choicesDiv.innerHTML = "";
  node.choices.forEach(choice => {
    const button = document.createElement("button");
    button.textContent = choice.text;
    button.onclick = () => showNode(choice.next);
    choicesDiv.appendChild(button);
  });
}

showNode("start");
