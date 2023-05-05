from flask import Flask, render_template, request
from backend import get_words, get_occupation2

app = Flask(__name__)

@app.route('/pathfinder', methods=['GET', 'POST'])
def button_cluster():
    # Define the list of keywords to the buttons:
    button_keywords = get_words()

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r') as fgreen:
        green_button_template = fgreen.read()
    with open('templates/orange_button_template.html', 'r') as forange:
        orange_button_template = forange.read()

    # Read the CSS code from the stylesheet:
    with open('templates/style copy.css', 'r') as stylesheet:
        css_read = stylesheet.read()

    # Generate the HTML code for the button cluster
    html = "<!DOCTYPE html><html><head>"
    html += css_read
    html += "</head><body><form method='post'>"
    for i, name in enumerate(button_keywords):
        template_index = i % 3
        if template_index == 0:
            template = blue_button_template
        elif template_index == 1:
            template = green_button_template
        else:
            template = orange_button_template
        button_html = template.format(name=name)
        html += f"<label for='checkbox_{i}'>{button_html}</label>"
        html += f"<input type='checkbox' name='checkbox_{i}' value='{name}'>"
    html += "<br><br>"
    html += "<input type='submit' value='Submit'>"
    html += "</form></body></html>"

    if request.method == 'POST':
        # Create list of checked button values
        checked_buttons = [request.form.get(f'checkbox_{i}') for i in range(len(button_keywords))]
        checked_buttons = [b for b in checked_buttons if b is not None]

        # Call function to get occupations based on checked buttons
        if len(checked_buttons) == 3:
            occupations = get_occupation2(*checked_buttons)
            print(f"Matching occupations: {occupations}")
        else:
            print("Please select exactly 3 keywords.")

    # Render the HTML code as a response
    return html

if __name__ == '__main__':
    app.run()
