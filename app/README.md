Bandersnatch Project

Overview

Bandersnatch is an interactive project combining Python, Flask, MongoDB, and machine learning to simulate a dynamic monster data management system. This application allows users to interact with a database of monsters, visualize their attributes, and predict their rarity using machine learning.

Features

Database Management:

Seed the database with randomly generated monster data.

Reset the database to remove all documents.

Retrieve documents as a Pandas DataFrame or HTML table.

Visualization:

Generate interactive visualizations of monster data using Plotly.

Machine Learning:

Train a machine learning model to predict monster rarity based on their attributes.

Save and load models for reuse.

Web Interface:

A Flask-based web interface for interacting with the database, visualizing data, and testing the machine learning model.

Table of Contents

Technologies Used

Installation

Usage

Modules and Functionality

Web Application Routes

Acknowledgments

Technologies Used

Python Libraries:

Flask: Web application framework.

pymongo: MongoDB connector.

pandas: Data manipulation and analysis.

plotly: Data visualization.

scikit-learn: Machine learning.

dotenv: Environment variable management.

Database:

MongoDB (Atlas).

Machine Learning Model:

Random Forest Classifier.

Frontend:

Flask templates and HTML.

Installation

Clone the repository:

git clone https://github.com/yourusername/bandersnatch.git
cd bandersnatch

Set up a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configure environment variables:

Create a .env file in the root directory with the following:

db_url=<Your MongoDB connection string>

Run the application:

python app.py

Usage

Database Interaction:

Seed, reset, or retrieve monster data using the Database class.

Visualization:

Generate a bar chart to visualize monster attributes with visualize_monsters().

Machine Learning:

Train and test a machine learning model to predict monster rarity using the Machine class.

Web Interface:

Access the Flask app via http://localhost:5000.

Modules and Functionality

1. Database

Handles all interactions with the MongoDB collection.

Methods:

seed(amount): Populate the database with random monster documents.

reset(): Delete all documents in the collection.

count(): Get the count of documents.

dataframe(): Retrieve all documents as a Pandas DataFrame.

html_table(): Retrieve documents as an HTML table.

visualize_monsters(): Generate a bar chart for monster attributes.

2. chart

Generates interactive Plotly scatterplots for data visualization.

3. Machine

Implements a Random Forest Classifier for predicting monster rarity.

Methods:

save(filepath): Save the trained model.

open(filepath): Load a pre-trained model.

info(): Get model metadata.

4. app.py

The main Flask application for rendering web pages and handling user requests.

Web Application Routes

/: Home page with random monster details.

/data: Displays monster data as an HTML table.

/view: Interactive visualization page for monster attributes.

/model: Predicts monster rarity based on user-provided attributes.

Acknowledgments

MongoDB Atlas for database hosting.

Plotly for powerful data visualization.

scikit-learn for machine learning capabilities.
