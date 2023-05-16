from backend import get_random_words


def replace_swedish_chars(text):
    html_entities = {
        "Ä": "&Auml;",
        "ä": "&auml;",
        "Ö": "&Ouml;",
        "ö": "&ouml;",
        "Å": "&Aring;",
        "å": "&aring;"
    }
    for char, entity in html_entities.items():
        text = text.replace(char, entity)
    return text

def replace_swedish_chars_list(list):
    changed_list = []
    for text in list:
        changed_text = replace_swedish_chars(text)
        changed_list.append(changed_text)
    return changed_list


testord = 'Jägare'
test2 = 'Jag älskar Sverige!'
test3 = 'Välj 5 som stämmer in med vem du är i arbetslivet!'
testlist = ['Jägare','Mördare', 'Mångsidig', 'Älskade', 'Önskade', 'Åkomma']

h1text = 'Här kan du välja 5 nyckelord som du känner passar in på dig som person och vad du kan tänka dig att göra!'
h4text = 'Utifrån dina valda nyckelord ger vi dig rekommendationer på yrkesval som vi tror kan passa dig.'
#print(testlist)
#reslist = replace_swedish_chars_list(testlist)
#print(reslist)
#print(replace_swedish_chars(test3))
print(replace_swedish_chars(h1text))
print(replace_swedish_chars(h4text))

# Define the list of keywords to the buttons:
#button_keywords_raw = get_random_words()
#print(button_keywords_raw)
#print()
# Replaces the swedish characters with HTML entities to display them properly on the website:
#button_keywords = replace_swedish_chars_list(button_keywords_raw)
#print(button_keywords)

# Swedish characters 
# Ä - &Auml;
# ä - &auml;
# Ö - &Ouml;
# ö - &ouml;
# Å - &Aring;
# å - &aring;