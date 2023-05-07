// Each button is generated in html as
//        <button class = 'circle-blue'>{name}</button> 
// where the placeholder represents the name/text in each button, i.e. the number 27 or the text "Social"

// The first button generated within the button container on the webpage is .button-container :nth-child(1) , the second button-container :nth-child(2) ....

// Get references to the buttons
var buttons = document.getElementsByTagName("button");

// Iterates over the buttons and adds event listeners to the buttons
for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", handleClick); 
}

// Handle button clicks
function handleClick(event) {
    // mark the button as clicked
    event.target.classList.toggle("focus");
}
 

