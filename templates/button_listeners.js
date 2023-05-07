
// Get references to the buttons
//const buttons = document.querySelectorAll('.circle-blue','circle-green','circle-orange');
//var button = document.getElementById("bluebutton")

// Add event listeners to the buttons
buttons.addEventListener('click', handleClick); 

// Handle button clicks
function handleClick(event) {
    // mark the button as clicked
    event.target.classList.add("focus");

    // save the state of the button to localStorage
    localStorage.setItem(event.target.id, "focus");
    }

// apply styles on page load based on saved button states
for (const i = 1; i<=51; i++) {
    const button = document.getElementById("button class='circle-orange'>" + i +"</button>");
    if (localStorage.getItem("button class='circle-orange'>" + i + "</button>") === "focus") {
        button.classList.add("focus");
    }
}

