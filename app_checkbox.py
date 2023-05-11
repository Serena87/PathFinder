from flask import Flask, render_template, request
from backend import get_random_words, get_occupation2
from swedish_chars_magic import replace_swedish_chars_list


app = Flask(__name__)

@app.route('/pathfinder', methods=['GET', 'POST'])
def button_cluster():
    # Define the list of keywords to the buttons:
    button_keywords_raw = get_random_words()
    # Replaces the swedish characters with HTML entities to display them properly on the website:
    button_keywords = replace_swedish_chars_list(button_keywords_raw)
    # gör tydligen ingen skillnad ändå...
    # fast det funkar att koda texten så med headern "Välj 5 etc.." och i "Vänligen välj exakt 5 ord" längst ner på sidan går det bra med vanliga åäö.."
    
    # Read the JavaScript code:
    with open('templates/button_listeners.js', 'r') as js:
       js_read = js.read()

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r') as fgreen:
        green_button_template = fgreen.read()
    with open('templates/orange_button_template.html', 'r') as forange:
        orange_button_template = forange.read()

    
    #Read the index html code for header from file:
    with open('templates/index_Stine.html', 'r') as index:
        header_read = index.read() # Read the index html code from file:
    
    # Read the CSS code from the stylesheet:
    with open('templates/style copy.css', 'r') as stylesheet:
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
            
            // Change button color based on checkbox state
            var button = event.currentTarget.querySelector("button");
            if (checkbox.checked) {
                button.classList.add("clicked");
            } else {
                button.classList.remove("clicked");
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
        }
       

        document.addEventListener('DOMContentLoaded', function() {
            var submitButton = document.querySelector("input[type='submit']");
            submitButton.addEventListener('click', function() {
                submitButton.classList.add('loading');   
            });
        });

    """
    html += "</script>"
    #html += "<script>"
    #html += js_read   # Denna kod gör inget ändå
    #html += "</script>"

    # End of head and start of html body
    html += "</head><body><form method='post'>"
    for i, name in enumerate(button_keywords):
        template_index = i % 3
        if template_index == 0:
            template = blue_button_template
        elif template_index == 1:
            template = green_button_template
        else:
            template = orange_button_template

        checkbox_html = f"<input type='checkbox' name='checkbox_{i}' value='{name}' style='display:none;'>"
        button_html = template.format(name=name)
        html += f"<label onclick='handleClick(event)'>{checkbox_html}<span class='button-label'>{button_html}</span></label>"
    # Reset and Submit buttons
    html += "<br><br>"
    html += "<input type='submit' value='Submit'>"
    html += "<input type='reset' value='Reset' onclick='handleReset(event)'>"
    html += "</form>"
   
    # Get the list of checked button values and display matching occupations
    if request.method == 'POST':
        # Create list of checked button values
        checked_buttons = [request.form.get(f'checkbox_{i}') for i in range(len(button_keywords))]
        checked_buttons = [b for b in checked_buttons if b is not None]

        # Call function to get occupations based on checked buttons
        if len(checked_buttons) == 5:
            occupations = get_occupation2(*checked_buttons)
            # Generate HTML code for matching occupations page
            match_html = render_template('occupations.html', occupations=occupations)
            return match_html
        elif len(checked_buttons) > 0:
            html += "<br><br>"
            html += "<h2>Vänligen välj exakt 5 nyckelord!</h2>"
    html += "<h3>Markerade nyckelord:</h3>"
    # counter for the number of chosen keywords
    html += "<div id='counter'>0</div>"
    html += "<script>"
    html += """
        
        const checkboxes = document.querySelectorAll("input[type='checkbox']");
        checkboxes.forEach((checkbox) => {
            checkbox.addEventListener('click', updateCounter());
        });

        function updateCounter() {
            // Get all the checkboxes
            const checkboxes = document.querySelectorAll("input[type='checkbox']");
            // Get the counter element
            const counter = document.getElementById("counter");
            // Count the number of selected checkboxes
            const selectedCount = Array.from(checkboxes).filter((checkbox) => checkbox.checked).length;
            // Update the text content of the counter element
            counter.textContent = selectedCount.toString();
        }

    """
    html += "</script>"
    html += "</body></html>"

    # Render the HTML code as a response
    return html

if __name__ == '__main__':
    app.run()









