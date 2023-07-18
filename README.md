# Springboard Capstone Project 

Welcome to my first capstone project — this application represents the culmination of my educational journey at the half-way point of Springboard's software engineering program. Here I have applied the concepts and techniques learned throughout the course, focusing on Python development and the suite of tools that we've learned alongside it.

## Project Overview

This full-stack application combines the skills and tools I've acquired to this point, including:
- Python
- Flask backend framework
- PostgreSQL for database management
- SQLAlchemy for ORM modeling
- Jinja templating engine in Flask
- TheMealDB API for external data fetching

The website design is all custom CSS and uses JavaScript and jQuery for some front-end functionality, such as a meal-plan builder shopping cart system. This project provided a real application instance of using JavaScript front-end code in conjunction with a Python back-end by using event triggers that send data back into the server to be stored and processed for dynamically updating the page.

## Getting Started

Here is a guide on how to get this app up and running on your local machine.

### Prerequisites

You will need to have the following installed on your machine:

- Python 3.10.6
- PostgreSQL
- Node.js and npm

### Installation

1. Clone this repository:

\`\`\`sh
git clone https://github.com/austindreosch/prepkitchen/
\`\`\`

2. Navigate to the project directory:

\`\`\`sh
cd prepkitchen
\`\`\`

3. Install Python dependencies:

\`\`\`sh
pip install -r requirements.txt
\`\`\`

4. Set up the PostgreSQL database:

\`\`\`sh
createdb prepkitchen
\`\`\`

5. Populate the database with data:

\`\`\`sh
python seed.py
\`\`\`

6. Start the Flask server:

\`\`\`sh
flask run
\`\`\`

Now the server should be running at `localhost:5000`.

### Usage

To make use of the application's features, follow these steps:

1. Go to `localhost:5000` on your web browser
2. Register a new account or login if you already have one
3. Browse the meal options and select the ones you want to add to your meal plan
4. Add them to your shopping cart
5. Checkout and you will receive a summary of your order

## Future Development

The journey doesn't stop here. Directly after this project, I begin work on the second half of the program, shifting the focus towards full-stack development with JavaScript using tools like React, Express, and Redux.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
