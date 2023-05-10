$(document).ready(function() { // when the page is loaded
    $('button').click(function() {  // when button is clicked
        $(this).toggleClass('clicked'); // toggled to clicked-class with another marking color
        var buttonName = $(this).text(); // extracts the name of the clicked button
        console.log(buttonName);   // prints the name of the clicked button in the web console
        });
    $('#resetBtn').click(function() {  // when clicking the reset button
       var allButtons = $('button');   // reference to all buttons
       $(allButtons).toggleClass('clicked',false); // toggles all buttons to original state, unclicked
    });
    $('#submitBtn').click(function() { // when clicking the submit button
        var clickedButtonNames = [];   // creates an empty list 
        $('button').each(function() {
            if ($(this).hasClass('clicked')) {
                //console.log($(this).text()); // printing the names in the console if the button is marked
                clickedButtonNames.push($(this).text()); // adds the names of each clicked button to the list 
            }
            //console.log(clickedButtonNames); // printing the populated array in console, works correctly!
        
        });
       
        $.ajax({ // ska skicka listan clickedButtonNames till python..
            url:'pathfinder',
            type: 'POST',
            data: { 'buttonWords' : clickedButtonNames},
            success: function(response) {
                console.log('Success!');
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
    

//document.addEventListener('DOMContentLoaded', handleClick() {

// Each button is generated in html as
//        <button class = 'colorbutton'>{name}</button> 
// where the placeholder represents the name/text in each button, i.e. the number 27 or the text "Social"

// The first button generated within the button container on the webpage is .button-container :nth-child(1) , the second button-container :nth-child(2) ....

    // Get references to the buttons
    //var buttons = document.getElementsByTagName("button");
    //const buttons = document.getElementsByTagName("button");
    //const clicked_buttons = buttons.getElementsByClassName("clicked");
    //var buttons = document.querySelector(".bluebutton");
    //const chosen_buttons = document.querySelectorAll(".clicked");

    // Iterates over the buttons and adds event listeners to the buttons
   // for (var i = 0; i < buttons.length; i++) {
   //     buttons[i].addEventListener("click", handleClick); 
   // }

    // Handle button clicks
    //function handleClick() {
    // mark the button as clicked
    //    buttons.classList.toggle("clicked");
   // }

 



