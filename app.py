from flask import Flask, render_template, request, redirect, url_for
from backend import get_occupation2, get_arbetsuppgifter, get_egenskaper, get_description
from list_work import list_mixer
import openai

#Lägg till egen nyckel! Om den ligger kvar/sparas och commitas förstörs den!!
openai.api_key = "" # Din privata nyckel

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

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r', encoding = 'utf-8') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r', encoding = 'utf-8') as fgreen:
        green_button_template = fgreen.read()

    # Read the index html code from file:
    with open('templates/index.html', 'r', encoding = 'utf-8') as index:
        html_read = index.read() 
    
    # Read the CSS code from the stylesheet:
    with open('templates/style.css', 'r', encoding = 'utf-8') as stylesheet:
        css_read = stylesheet.read()

    # Start HTML code
    html = html = html_read # Reads from html file (including JavaScript code)
    html += css_read  # Reads from CSS file
    
    # HTML code for the request form containing the bubbles and submit/reset buttons
    html += "<div class='button-container'>"
    # Generate the HTML code for the button cluster and creates hidden checkboxes spanning over the buttons:
    for i, name in enumerate(button_keywords_mixed):
        template_index = i % 2
        if template_index == 0:
            template = blue_button_template
            button_keywords = button_keywords_attributes
        else:
            template = green_button_template
            button_keywords = button_keywords_tasks
        
        checkbox_html = f"<input type='checkbox' name='checkbox_{i}' value='{button_keywords[i//2]}' style='display:none;'>"
        button_html = template.format(name=button_keywords[i//2])
        html += f"<label onclick='handleClick(event)'>{checkbox_html}<span class='button-label'>{button_html}</span></label>"
    html += "</div>"
    html += "<br><br>"
    html += "</form>" # End of request form
   
    # Get the list of checked button values and display matching occupations
    if request.method == 'POST':
        # Create list of checked button values
        checked_buttons = [request.form.get(f'checkbox_{i}') for i in range(len(button_keywords_mixed))]
        checked_buttons = [b for b in checked_buttons if b is not None]
        
        # Call function to get occupations based on checked buttons
        if len(checked_buttons) == 5:
            occupations = get_occupation2(*checked_buttons)
            # Generate HTML code for matching occupations page
            match_html = render_template('occupations.html', occupations=occupations)
            return match_html
        
    html += "</body></html>" # END of the whole HTML code

    # Render the HTML code as a response
    return html

# Ny route som hanterar requests
@app.route('/occupation_description', methods=['POST'])
def occupation_description():
    if request.method == 'POST':
        occupation = request.form.get('occupation')
        description = get_description(occupation)

        return description

if __name__ == '__main__':
    app.run()










