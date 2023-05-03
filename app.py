
    
from flask import Flask, render_template
from backend import get_words

app = Flask(__name__)

@app.route('/pathfinder')
def button_cluster():
    # Define the list of keywords to the buttons:
    button_keywords = get_words()
    #button_keywords = get_words()
    button_templates = ["blue_button_template", "green_button_template", "orange_button_template"]

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r') as fgreen:
        green_button_template = fgreen.read()
    with open('templates/orange_button_template.html', 'r') as forange:
        orange_button_template = forange.read()
    with open('templates/style.css', 'r') as stylesheet:
        css_read = stylesheet.read()

    # Generate the HTML code for the button cluster
    html = "<!DOCTYPE html><html><head>"
    html += css_read
    html += "</head><body><div class='button-cluster'>"
    for i, name in enumerate(button_keywords):
        template_index = i % len(button_templates)
        template = button_templates[template_index]
        if template == "blue_button_template":
            button_html = blue_button_template.format(name=name)
        elif template == "green_button_template":
            button_html = green_button_template.format(name=name)
        else:
            button_html = orange_button_template.format(name=name)
        html += button_html
    html += "</div></body></html>"

    # Render the HTML code as a response
    return html

if __name__ == '__main__':
    app.run()
