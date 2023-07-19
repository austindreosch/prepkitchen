# Springboard Capstone Project 

Welcome to my first capstone project — this application represents the culmination of my educational journey at the half-way point of Springboard's software engineering program. Here I have applied the concepts and techniques learned throughout the course, focusing on Python development and the suite of tools that we've learned alongside it.

## Project Overview

This full-stack application combines the skills and tools I've acquired to this point, including:
- Python
- Flask backend framework
- PostgreSQL for database management
- SQLAlchemy for ORM modeling
- Jinja templating engine
- TheMealDB API for external data fetching

The website design is also made with all custom CSS, and makes use of JavaScript and jQuery for some front-end functionality, such as the meal-plan builder shopping cart system - which sends client-side data to an API point on the Flask server to synchronize the local storage cache data with the user's session data, and updates the displayed shopping cart automatically. I was particularly proud of this implementation - as it was my first real application instance of independently tackling the complex conceptual challenge around how to use JavaScript front-end code in conjunction with a Python back-end by using event triggers that send data back into the server to be stored and processed for dynamically updating the page.

## Getting Started

Here is a guide on how to get this app up and running on your local machine.

### Prerequisites

You will need to have the following installed on your machine:

- Python 3.10.6
- PostgreSQL

### Installation

1. Clone this repository:

git clone https://github.com/austindreosch/prepkitchen/

2. Navigate to the project directory:

cd prepkitchen

3. Install Python dependencies:

pip install -r requirements.txt

4. Set up the PostgreSQL database:

createdb prepkitchen

5. Populate the database with data:

python seed.py

6. Start the Flask server:

flask run

Now the server should be running at `localhost:5000`.

### Usage

To make use of the application's features, follow these steps:

1. Go to `localhost:5000` on your web browser
2. Register a new account or login if you already have one
3. Browse the meal options and select the ones you want to add to your meal plan
4. Add them to your shopping cart
5. Checkout and you will receive a summary of your orders in your profile page.
