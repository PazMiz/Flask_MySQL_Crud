Flask MySQL CRUD
This is a simple Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations using MySQL as the database.

Prerequisites
Python (version 3.6 or higher)
Flask (install using pip install flask)
MySQL (install and set up on your machine)
Installation
Clone the repository to your local machine.
Create a virtual environment (optional but recommended).
Install the required packages using pip install -r requirements.txt.
Update the MySQL configuration in the app.py file with your database credentials.
Database Setup
Create a new database in MySQL for this application.
Update the mysql_config dictionary in the app.py file with your database credentials and database name.
Running the Application
To run the application, execute the following command in your terminal or command prompt:

Copy code
python app.py

Endpoints
GET /cars: Fetch all car records from the database.
POST /create_car: Create a new car record in the database. Send a JSON object with the "model" and "color" fields in the request body.
PUT /update_car: Update an existing car record in the database. Send a JSON object with the "id", "model", and "color" fields in the request body.
DELETE /delete_car/:id: Delete a car record from the database with the given ID.
