

from flask import Flask, render_template
from backend import get_words

app = Flask(__name__)

@app.route('/pathfinder')
def button_cluster():
    # Define the list of keywords to the buttons:
    button_keywords = ["Musik", "Fotografera", "Design", "Social"]
    #button_keywords = get_words()
    button_templates = ["blue_button_template", "green_button_template", "orange_button_template"]

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r') as fgreen:
        green_button_template = fgreen.read()
    with open('templates/orange_button_template.html', 'r') as forange:
    # Read the CSS style for the buttons and the cluster from file:    
        orange_button_template = forange.read()
    with open('templates/style.css', 'r') as stylesheet:
        css_read = stylesheet.read()

    # Generate the HTML code for the button cluster
    x = 0
    html = "<!DOCTYPE html><html><head>"
    html += css_read
    html += "</head><body><div class='button-cluster'>"
    for name in button_keywords:
        button_html = green_button_template.format(name=name)
        #button = button_templates(x)
        #button_html = button 
        #button_html += ".format(name=name)"
        html += button_html
        x += 1
    html += "</div></body></html>"

    # Render the HTML code as a response
    return html

if __name__ == '__main__':
    app.run()
    