from flask import Flask, render_template
#from backend import get_words

app = Flask(__name__)

@app.route('/pathfinder')


def index():
    # Refer to/read the JavaScript file used: TODO DOESN`T WORK..
    #js_file = 'templates/button_listeners.js'

    with open('templates/button_listeners.js', 'r') as js:
        js_read = js.read()

    # Define the list of keywords to the buttons:
    #button_keywords = get_words()
 
    # For adjusting the buttons, easier with 50 numbers
    button_keywords = []
    for i in range(1, 51):
        button_keywords.append(str(i))
   
    button_templates = ["blue_button_template", "green_button_template", "orange_button_template"]

    # Read the button templates from the html files:
    with open('templates/blue_button_template.html', 'r') as fblue:
        blue_button_template = fblue.read()
    with open('templates/green_button_template.html', 'r') as fgreen:
        green_button_template = fgreen.read()
    with open('templates/orange_button_template.html', 'r') as forange:
        orange_button_template = forange.read()

    # Read the index html code from file:
    with open('templates/index_Stine.html', 'r') as index:
        header_read = index.read() # Read the index html code from file:
    
    # Read the CSS code from the stylesheet:
    with open('templates/style copy.css', 'r') as stylesheet:
        css_read = stylesheet.read()

    # Generates the HTML code for the website:
    html = header_read
    #html += js_read
    html += css_read
    html += "<div class='button-container'>"
    # Generates the keyword buttons: 
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
    #return render_template('index_Stine.html')

if __name__ == '__main__':
    app.run()
