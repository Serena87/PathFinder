from flask import Flask, render_template, request, redirect, url_for
import time
from backend import get_occupation2, get_arbetsuppgifter, get_egenskaper
from list_work import list_mixer
import random
from chatintegration import get_description



app = Flask(__name__)

@app.route('/pathfinder')
def intro_page():
    return render_template('intro.html')


@app.route('/pathfinder_main', methods=['GET', 'POST'])
def button_cluster():
    # Define the list of keywords to the buttons:
    
    button_keywords_attributes = get_egenskaper() # from backend, list with 15 personal attributes
    button_keywords_tasks = get_arbetsuppgifter() # from backend, list with 15 work tasks
    button_keywords_mixed = list_mixer(button_keywords_attributes, button_keywords_tasks) # adding the two lists together to new list with 30 words
    random.shuffle(button_keywords_mixed) # Shuffles the words in the list so that they are mixed before creating the buttons/bubbles with the list

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r', encoding = 'utf-8') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r', encoding = 'utf-8') as fgreen:
        green_button_template = fgreen.read()

    #Read the index html code for header from file:
    with open('templates/index.html', 'r', encoding = 'utf-8') as index:
        header_read = index.read() # Read the index html code from file:
    
    # Read the CSS code from the stylesheet:
    with open('templates/style.css', 'r', encoding = 'utf-8') as stylesheet:
        css_read = stylesheet.read()

    # Generate the HTML code for the button cluster
    html = html = header_read
    html += css_read
    html += "<script>"
    html += """
       
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

    """
    html += "</script>"
   
    # End of head and start of html body
    html += "</head><body>"
    html += "<form method='post'>"
    html += "<div class='button-container'>"
    for i, name in enumerate(button_keywords_mixed):
        template_index = i % 2
        if template_index == 0:
            template = blue_button_template
            button_keywords = button_keywords_attributes
        else:
            template = green_button_template
            button_keywords = button_keywords_tasks

        checkbox_html = f"<input type='checkbox' name='checkbox_{i}' value='{name}' style='display:none;'>"
        button_html = template.format(name=button_keywords[i//2])
        html += f"<label onclick='handleClick(event)'>{checkbox_html}<span class='button-label'>{button_html}</span></label>"
    html += "</div>"
    html += "<br><br>"
    
    # Reset and Submit buttons
    html += "<input type='submit' value='Submit'>"
    html += "<input type='reset' value='Reset' onclick='handleReset(event)'>"
    html += "</form>"
   
    # Get the list of checked button values and display matching occupations
    if request.method == 'POST':
        # Create list of checked button values
        checked_buttons = [request.form.get(f'checkbox_{i}') for i in range(len(button_keywords_mixed))]
        checked_buttons = [b for b in checked_buttons if b is not None]

        # Call function to get occupations based on checked buttons
        if len(checked_buttons) == 5:
            occupations = get_occupation2(*checked_buttons)
            # Generate HTML code for matching occupations page
            match_html = render_template('occupationsjon.html', occupations=occupations)
            return match_html
        elif len(checked_buttons) > 0:
            html += "<br><br>"
            html += "<h2>Vänligen välj exakt 5 nyckelord!</h2>"


    html += "</body></html>"

    # Render the HTML code as a response
    return html



if __name__ == '__main__':
    app.run()










