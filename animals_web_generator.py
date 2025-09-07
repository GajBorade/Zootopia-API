import requests

API_KEY = "vhsMl65OlbqlcLampKsQNA==NITMWEkASilQuoif"
REQUEST_URL = f"https://api.api-ninjas.com/v1/animals?name="
HEADERS = {"X-Api-Key": API_KEY}


def load_data(animal_name):
    """
    loads the data from the api

    :param animal_name: name of the animal
    :return:list of nested dictionaries representing animal data
    """
    res = requests.get(REQUEST_URL + animal_name, headers=HEADERS)
    if res.status_code != 200:
        print(f"Request failed with status code {res.status_code}")
    else:
        return res.json()
    return []


def get_animal_data():
    """
    Prompts the user to enter an animal name and fetches data from the API once.

    This function does not attempt retries or provide a default animal.
    The returned list may be empty if the API does not find the animal.
    :return: list of dictionaries containing animal data
    """
    animal_name = input("Enter animal name: ").strip().lower()
    animals_data = load_data(animal_name)
    return animal_name, animals_data


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
    - Loads animal data from response API
    - Prints animals data to console
    - Reads HTML template
    - Serializes animal data into HTML list items
    - Writes final HTML file to disk

    :return: None
    """
    # Load animal data from api ninjas
    animals_name, animals_data = get_animal_data()

    # Read HTML template
    animals_template_path = "animals_template.html"
    animals_template_html = read_html_template(animals_template_path)

    if animals_data:
        final_html = animals_template_html.replace(
            "__REPLACE_ANIMALS_INFO__", serialize_animals_data(animals_data)
        )
    else:
        final_html = animals_template_html.replace(
            "__REPLACE_ANIMALS_INFO__",
            f'<h2>The animal "{animals_name}" does not exist.</h2>',
        )

    # Write final HTML to file
    write_html_template(final_html)


if __name__ == "__main__":
    main()
