# Zootopia API – Animal Website Generator 🐾

This project fetches animal data from the API Ninjas Animals API and generates 
a simple HTML website to display the information.

## Installation

Clone the repository:

git clone <your-repo-url>
cd Zootopia-API

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Add your API key in a .env file at the root of the project:

API_KEY='your_api_key_here'

## Usage

Run the program with:

python animals_web_generator.py

Enter the name of an animal when prompted. A file animals.html will be generated. 
Open it in your browser to view the animal information.

## Contributing

We welcome contributions! Please follow standard Python development practices:

1. Fork the repository  
2. Create a branch for your feature or fix  
3. Submit a pull request with a clear description of changes

## Dependencies

requests – For API calls  
python-dotenv – To load API key from .env

