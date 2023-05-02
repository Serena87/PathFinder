from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pathfinder')
def button_cluster():
    # Define the list of keywords to the buttons:
    button_keywords = ["Musik", "Fotografera", "Design", "Social"]
    #button_type = ["circle-blue", "circle-green", "circle-orange"]

    # Read the button template from the html file index_Stine.html:
    with open('templates/blue_button_template.html', 'r') as fblue:
        blue_button_template = fblue.read()
    
    with open('templates/style.css', 'r') as stylesheet:
        css_read = stylesheet.read()

    # Generate the HTML code for the button cluster
    html = "<!DOCTYPE html><html><head>"
    html += css_read
    html += "</head><body><div class='button-cluster'>"
    for name in button_keywords:
        button_html = blue_button_template.format(name=name)
        html += button_html
    html += "</div></body></html>"

    # Render the HTML code as a response
    return html

if __name__ == '__main__':
    app.run()


    