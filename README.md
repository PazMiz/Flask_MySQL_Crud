# Car Management API with Flask and MySQL

This project implements a basic Flask API for managing car data in a MySQL database. It allows you to perform CRUD (Create, Read, Update, Delete) operations on car records.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.6 or later)
- Flask (install via pip: `pip install Flask`)
- MySQL Server

## Getting Started

1. Clone the repository to your local machine.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


## 

python app.py



Endpoints
1. Create Car
Endpoint: POST /create_car

This endpoint allows you to create car records in the database.

Request Format:

json
Copy code
{
  "cars": [
    {
      "model": "Car Model 1",
      "color": "Red"
    },
    {
      "model": "Car Model 2",
      "color": "Blue"
    },
    ...
  ]
}
Response:

Status Code: 200 (OK) if the data was inserted successfully.
Status Code: 500 (Internal Server Error) if an error occurs during insertion.
2. Get Cars
Endpoint: GET /cars

This endpoint retrieves all car records from the database and returns them as JSON.

Response Format:

json
Copy code
[
  {
    "id": 1,
    "model": "Car Model 1",
    "color": "Red"
  },
  {
    "id": 2,
    "model": "Car Model 2",
    "color": "Blue"
  },
  ...
]
3. Update Car
Endpoint: POST /update_car

This endpoint allows you to update existing car records in the database.

Request Format:

json
Copy code
{
  "cars": [
    {
      "id": 1,
      "model": "Updated Model 1",
      "color": "Green"
    },
    {
      "id": 2,
      "model": "Updated Model 2",
      "color": "Yellow"
    },
    ...
  ]
}
Response:

Status Code: 200 (OK) if the data was updated successfully.
Status Code: 500 (Internal Server Error) if an error occurs during update.
4. Delete Car
Endpoint: POST /delete_car

This endpoint allows you to delete a car record from the database.

Request Format:

json
Copy code
{
  "car_id": 1
}
Response:

Status Code: 200 (OK) if the data was deleted successfully.
Status Code: 500 (Internal Server Error) if an error occurs during deletion.
