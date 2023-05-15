// JavaScript code for handling the buttons

function handleClick(event) {
    event.preventDefault();
    var checkbox = event.currentTarget.querySelector("input[type=checkbox]");
    checkbox.checked = !checkbox.checked;

        var count = parseInt(document.getElementById("counter").innerHTML); // Gets the current counter value

            // Change button color based on checkbox state
            var button = event.currentTarget.querySelector("button");
            if (checkbox.checked) {
                count += 1;
                document.getElementById("counter").innerHTML = count;
                button.classList.add("clicked");
                moveSelectedButton(button); // Move the clicked button to selected keywords
            
            } else {
                count -= 1;
                document.getElementById("counter").innerHTML = count;
                button.classList.remove("clicked");
                removeSelectedButton(button); // Remove the button from selected keywords
            }
            
        }
        function moveSelectedButton(button) {
            var selectedContainer = document.getElementById("selected_keywords");
            var clonedButton = button.parentNode.cloneNode(true);
            var originalButton = clonedButton.querySelector("button");
            originalButton.classList.remove("clicked");
            selectedContainer.appendChild(clonedButton);
        
        }
        function removeSelectedButton(button) {
            var selectedContainer = document.getElementById("selected_keywords");
            var buttons = selectedContainer.querySelectorAll("button");
            for (var i = 0; i < buttons.length; i++) {
                if (buttons[i].textContent === button.textContent) {
                    selectedContainer.removeChild(buttons[i].parentNode);
                    break;
                }
            }
        }
        function handleReset(event) {
            event.preventDefault();
            var checkboxes = document.querySelectorAll("input[type=checkbox]");
            for (var i = 0; i < checkboxes.length; i++) {
                checkboxes[i].checked = false;
            }
            
            // Remove button color classes
            var buttons = document.querySelectorAll("button");
            for (var i = 0; i < buttons.length; i++) {
                buttons[i].classList.remove("clicked");
            }
            // Clear selected keywords
            var selectedContainer = document.getElementById("selected_keywords");
            selectedContainer.innerHTML = "";

            document.getElementById("counter").innerHTML = 0;
        
        };

