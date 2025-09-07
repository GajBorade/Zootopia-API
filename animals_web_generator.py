import json


def load_data(file_path):
    """
    Loads data from json file

    :param file_path: Path to json file
    :return: list of nested dictionaries representing data
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


# 1. Read the contents of the template, animals_template.html
def read_html_template(template_path):
    """
    Reads an HTML template from a file.

    :param template_path: Path to the HTML template file.
    :return: Content of the template file as a string.
    """
    with open(template_path, "r", encoding="utf-8") as fileobject:
        return fileobject.read()


# 2. Generate a string with the animals’ data
# Use HTML tags & wrap animals in block elements p
def serialize_animals_data(animals_obj):
    """
    Serializes a list of animals into HTML list items,
    skipping any missing fields.

    :param animals_obj: list of nested dictionaries, each representing an animal.
    :return: A string containing HTML representation of all animals
    """
    output = ""
    for animal in animals_obj:
        output += f'    <li class="cards__item">\n'
        output += f'        <div class="card__title">{animal.get("name", "")}</div>\n'
        output += f'        <div class="card__text">\n'
        output += f'            <ul class="card_details">\n'

        characteristics = animal.get("characteristics", {})

        # Helper: add <li> only if field exists
        def add_li(label, value):
            return (
                f'                <li class="card_detail"><strong>{label}</strong>: {value}</li>\n'
                if value
                else ""
            )

        # Standard fields
        output += add_li("Diet", characteristics.get("diet"))
        output += add_li("Type", characteristics.get("type"))

        # Locations
        locations = animal.get("locations")
        if locations:
            output += add_li("Location", locations[0])

        # Bonus fields
        output += add_li("Life-span", characteristics.get("lifespan"))
        output += add_li("Habitat", characteristics.get("habitat"))
        output += add_li("Slogan", characteristics.get("slogan"))
        output += add_li("Color", characteristics.get("color"))
        output += add_li("Speed", characteristics.get("top_speed"))
        output += add_li("Temperament", characteristics.get("temperament"))

        output += f"            </ul>\n"
        output += f"        </div>\n"
        output += f"    </li>\n"
    return output


# Step 4. Write this new string to the 'new' html file
def write_html_template(html_data):
    """
    Writes the given HTML content (str) to the 'animals.html' file.

    :param html_data: A string containing the full HTML content (str)
    to be written to the file.
    :return: None
    """
    with open("animals.html", "w", encoding="utf-8") as fileobject:
        fileobject.write(html_data)


def main():
    """
    Controls the flow of the program:
    - Loads animal data from JSON
    - Prints animals data to console
    - Reads HTML template
    - Serializes animal data into HTML list items
    - Writes final HTML file to disk

    :return: None
    """
    # Load animal data from json file
    filename = "animals_data.json"
    animals_data = load_data(filename)

    # Read HTML template
    animals_template_path = "animals_template.html"
    animals_template_html = read_html_template(animals_template_path)

    # Step 3: Replace __REPLACE_ANIMALS_INFO__ with the generated string
    # to serialize animals into HTML
    final_html = animals_template_html.replace(
        "__REPLACE_ANIMALS_INFO__", serialize_animals_data(animals_data)
    )

    # Write final HTML to file
    write_html_template(final_html)


if __name__ == "__main__":
    main()
