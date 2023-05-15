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
        var selectedBoxes = $("input[type='checkbox']:checked"); // get all checked/clicked buttons/checkboxes
        var checkedValues = []; // creates an empty array to store the values
        selectedBoxes.each(function() { // loop through checked boxes
            checkedValues.push($(this).val());
        });
        console.log(checkedValues); // for checking
        // show loading animation
        $('#submitBtn').addClass('loading');
    
    $.ajax({
        url:'/pathfinder',
        type: 'POST',
        data: { checkedWords : checkedValues},
        success: function(response) {
            console.log(response); // handle response from server
        },
        error: function(error) {
            console.log('Error: ' + error);
        },
        complete: function() {
            // remove loading animation
            $('#submitBtn').removeClass('loading');
        }
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

 



